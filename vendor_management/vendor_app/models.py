from django.db import models
from django.db.models import Avg, Count

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    def calculate_on_time_delivery_rate(self):
        completed_pos = self.purchaseorder_set.filter(status='completed')
        on_time_deliveries = completed_pos.filter(delivery_date__lte=models.F('acknowledgment_date'))
        return (on_time_deliveries.count() / completed_pos.count()) * 100 if completed_pos.count() > 0 else 0

    def calculate_quality_rating_avg(self):
        completed_pos = self.purchaseorder_set.filter(status='completed', quality_rating__isnull=False)
        return completed_pos.aggregate(Avg('quality_rating'))['quality_rating__avg'] or 0

    def calculate_average_response_time(self):
        acknowledged_pos = self.purchaseorder_set.filter(acknowledgment_date__isnull=False)
        response_times = [(po.acknowledgment_date - po.issue_date).total_seconds() for po in acknowledged_pos]
        return sum(response_times) / len(response_times) if len(response_times) > 0 else 0


    def calculate_fulfillment_rate(self):
        all_pos = self.purchaseorder_set.all()
        fulfilled_pos = all_pos.filter(status='completed')
        return (fulfilled_pos.count() / all_pos.count()) * 100 if all_pos.count() > 0 else 0

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.CharField(max_length=250)
    quantity = models.IntegerField()
    status = models.CharField(max_length=50)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='historical_performances')
    date = models.DateTimeField(null=True, blank=True)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()
