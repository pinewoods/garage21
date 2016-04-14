import json

from django.test import TestCase
from django.test import Client

from django.contrib.auth.models import User

from .models import GasCylinder
from .models import CylinderWeight


class GasTestCase(TestCase):

    fixtures = ['gas/test_user.json']

    def setUp(self):
        self.client = Client()
        #response = self.client.post('/login/', {'username': 'john', 'password': 'smith'})

        self.user = User.objects.get(pk=1)
        gc = GasCylinder(user=self.user)
        gc.save()

    def test_api_post(self):

        device_msg = {
                'channel': 1,
                'weight': 10.0,
        }

        response = self.client.post(
                '/gas/api/',
                json.dumps(device_msg),
                content_type='application/json'
        )
        self.assertEqual(response.status_code, 204)
