from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Invoice

class InvoiceAPITestCase(APITestCase):
    def test_create_invoice(self):
        url = reverse('invoice-list-create')
        data = {'date': '2024-04-16', 'customer_name': 'Test Customer'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Invoice.objects.count(), 1)
    
    def test_get_invoice(self):
        invoice = Invoice.objects.create(date='2024-04-16', customer_name='Test Customer')
        url = reverse('invoice-retrieve-update-destroy', kwargs={'pk': invoice.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    # Write similar test cases for update, delete, and other endpoints
