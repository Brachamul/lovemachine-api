from django.test import TestCase, Client
from django.urls import reverse

from android_apps.search import search_play_store

from android_apps.models import AndroidApp



class AddAppsThroughSearchTestCase(TestCase):

	def test_new_apps_created(self):
		search_play_store('pota')
		stored_apps = AndroidApp.objects.all()
		self.assertIs(stored_apps.count() > 0, True)