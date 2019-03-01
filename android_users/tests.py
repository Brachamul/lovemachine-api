from django.test import TestCase, Client
from django.urls import reverse

from .models import AndroidUser



class GetOrCreateUserTestCase(TestCase):

	def setUp(self):
		self.client = Client()

	def test_create_user(self):
		gsps_id = "bob"
		url = reverse('android_users__user_get_or_create') + "?google_gamer_id=bob"
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)

	def test_get_user(self):
		pass