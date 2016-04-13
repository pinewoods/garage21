from django.test import TestCase
from django.test import Client

from .models import GasCylinder
from .models import CylinderWeight

class GasTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        #response = self.client.post('/login/', {'username': 'john', 'password': 'smith'})

    def test_api_post(self):
        response = self.client.post('/gas/api')
        self.assertEqual(response.status_code, 204)
