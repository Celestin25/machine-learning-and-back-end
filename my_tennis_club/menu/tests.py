from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Menu

class MenuTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.create_url = reverse('create-menu-item')
        self.get_url = reverse('get-menu-items')
        self.update_url = lambda item_id: reverse('update-menu-item', args=[item_id])
        self.delete_url = lambda item_id: reverse('delete-menu-item', args=[item_id])
        self.menu_item = {'name': 'Pizza', 'price': '10.00', 'quantity': 100}
    
    def test_create_menu_item(self):
        response = self.client.post(self.create_url, self.menu_item, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], 'Menu item created successfully')
    
    def test_get_menu_items(self):
        self.client.post(self.create_url, self.menu_item, format='json')
        response = self.client.get(self.get_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Pizza', [item['name'] for item in response.data])
    
    def test_update_menu_item(self):
        item = Menu.objects.create(**self.menu_item)
        update_data = {'name': 'Updated Pizza', 'price': '12.00', 'quantity': 150}
        response = self.client.put(self.update_url(item.item_id), update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Menu item updated successfully')
    
    def test_delete_menu_item(self):
        item = Menu.objects.create(**self.menu_item)
        response = self.client.delete(self.delete_url(item.item_id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Menu item deleted successfully')
