from rest_framework import generics
from rest_framework.response import Response
from django.utils import timezone
from .models import Vendor, PurchaseOrder, HistoricalPerformance
from .serializers import VendorSerializer, PurchaseOrderSerializer, HistoricalPerformanceSerializer

class VendorListCreateView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class VendorPerformanceView(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = HistoricalPerformanceSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        performance_data = {
            'on_time_delivery_rate': instance.calculate_on_time_delivery_rate(),
            'quality_rating_avg': instance.calculate_quality_rating_avg(),
            'average_response_time': instance.calculate_average_response_time(),
            'fulfillment_rate': instance.calculate_fulfillment_rate(),
        }
        serializer = self.get_serializer(data=performance_data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)
    

class AcknowledgePurchaseOrderView(generics.UpdateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.acknowledgment_date = timezone.now()
        instance.save()
        return Response({'detail': 'Purchase Order acknowledged successfully.'})
