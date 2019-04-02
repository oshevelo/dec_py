from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
import time
from apps.products.models import Product

class ProductListAPITest(TestCase):

    def setUp(self):
        print('setUp')
        self.c = APIClient()
        #p = Product.objects.create(name='ttt', price=123)

    def test_list(self):        
        #time.sleep(123123)
        p = Product.objects.create(name='ttt', price=123)
        response = self.c.get(
            '/products/all/'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_list2(self):
        #time.sleep(123123)
        response = self.c.get(
            '/products/all/'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

class ListAPITest(TestCase):

    def setUp(self):
        print('setUp')
        self.c = APIClient()
        #p = Product.objects.create(name='ttt', price=123)

    def test_list(self):        
        #time.sleep(123123)
        p = Product.objects.create(name='ttt', price=123)
        response = self.c.get(
            '/products/all/'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_list2(self):
        #time.sleep(123123)
        response = self.c.get(
            '/products/all/'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

class PListAPITest(TestCase):

    def setUp(self):
        print('setUp')
        self.c = APIClient()
        #p = Product.objects.create(name='ttt', price=123)

    def test_list(self):        
        #time.sleep(123123)
        p = Product.objects.create(name='ttt', price=123)
        response = self.c.get(
            '/products/all/'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_list2(self):
        #time.sleep(123123)
        response = self.c.get(
            '/products/all/'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
