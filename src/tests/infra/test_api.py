from unittest.mock import patch

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from core.entities.company import CompanyEntity
from infra.api import BaseView


class MockController:
    def create_object(self, params):
        pass

    def detail_object(self, object_id):
        pass

    def update_object(self, params):
        pass


class BaseViewAPITestCase(APITestCase):
    def setUp(self):
        self.view = BaseView()
        self.view.controller = MockController()

    def test_dispatch_with_invalid_model(self):
        url = reverse('create', kwargs={'model': 'invalid'})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_company(self):
        url = reverse('create', kwargs={'model': 'company'})
        data = {
            "street": "Street",
            "city": "City",
            "country": "Country",
            "cnpj": "74422843000112",
        }

        with patch(
            "app.controller.CompanyController.create_object",
            return_value=CompanyEntity(
                **{
                    "street": "Street",
                    "city": "City",
                    "country": "Country",
                    "cnpj": "74422843000112",
                }
            ),
        ), patch(
            "rest_framework.permissions.IsAdminUser.has_permission",
            return_value=True,
        ):
            response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data = response.data
        print(data['error'])
        self.assertTrue(data['success'])
        self.assertIsNone(data['error'])
        self.assertEqual(
            data['data'],
            {
                'city': 'City',
                'cnpj': '74422843000112',
                'country': 'Country',
                'created_at': None,
                'id': None,
                'is_active': True,
                'street': 'Street',
                'updated_at': None,
            },
        )
