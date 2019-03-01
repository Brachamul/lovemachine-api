from django.urls import include, path

from . import calls



urlpatterns = [
	path('get_or_create/', calls.get_or_create, name='android_users__get_or_create'),
]