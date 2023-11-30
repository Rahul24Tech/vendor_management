from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Vendor, PurchaseOrder

class VendorAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.vendor = Vendor.objects.create(
            name="Vendor Test",
            contact_details="Contact Test",
            address="Address Test",
            vendor_code="V001",
        )
        self.purchase_order = PurchaseOrder.objects.create(
            po_number="PO001",
            vendor=self.vendor,
            order_date="2023-01-01T00:00:00Z",
            delivery_date="2023-01-15T00:00:00Z",
            items={"item": "Test Item"},
            quantity=10,
            status="completed",
            quality_rating=4.5,
            issue_date="2023-01-01T00:00:00Z",
            acknowledgment_date="2023-01-02T00:00:00Z",
        )

    def test_vendor_endpoints(self):
        # Test create a new vendor
        create_vendor_data = {
            "name": "New Vendor",
            "contact_details": "New Contact",
            "address": "New Address",
            "vendor_code": "V002",
        }
        response = self.client.post(reverse("vendor-list-create"), create_vendor_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Test list all vendors
        response = self.client.get(reverse("vendor-list-create"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test retrieve a specific vendor
        response = self.client.get(reverse("vendor-retrieve-update-delete", args=[self.vendor.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test update a vendor
        update_vendor_data = {"name": "Updated Vendor"}
        response = self.client.put(reverse("vendor-retrieve-update-delete", args=[self.vendor.id]), update_vendor_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test delete a vendor
        response = self.client.delete(reverse("vendor-retrieve-update-delete", args=[self.vendor.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_purchase_order_endpoints(self):
        # Test create a new purchase order
        create_po_data = {
            "po_number": "PO002",
            "vendor": self.vendor.id,
            "order_date": "2023-02-01T00:00:00Z",
            "delivery_date": "2023-02-15T00:00:00Z",
            "items": {"item": "New Item"},
            "quantity": 5,
            "status": "pending",
            "issue_date": "2023-02-01T00:00:00Z",
        }
        response = self.client.post(reverse("purchase-order-list-create"), create_po_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Test list all purchase orders
        response = self.client.get(reverse("purchase-order-list-create"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test retrieve details of a specific purchase order
        response = self.client.get(reverse("purchase-order-retrieve-update-delete", args=[self.purchase_order.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test update a purchase order
        update_po_data = {"status": "completed"}
        response = self.client.put(reverse("purchase-order-retrieve-update-delete", args=[self.purchase_order.id]), update_po_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test delete a purchase order
        response = self.client.delete(reverse("purchase-order-retrieve-update-delete", args=[self.purchase_order.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_vendor_performance_endpoint(self):
        # Test retrieve performance metrics for a specific vendor
        response = self.client.get(reverse("vendor-performance", args=[self.vendor.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("on_time_delivery_rate", response.data)
        self.assertIn("quality_rating_avg", response.data)
        self.assertIn("average_response_time", response.data)
        self.assertIn("fulfillment_rate", response.data)

    def test_acknowledge_purchase_order_endpoint(self):
        # Test acknowledge a purchase order
        response = self.client.get(reverse("acknowledge-purchase-order", args=[self.purchase_order.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if acknowledgment_date is updated
        updated_purchase_order = PurchaseOrder.objects.get(id=self.purchase_order.id)
        self.assertIsNotNone(updated_purchase_order.acknowledgment_date)
