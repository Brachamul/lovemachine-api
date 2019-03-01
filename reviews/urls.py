from django.urls import include, path

from . import calls



urlpatterns = [
	path('rate/', calls.rate, name='ratings__rate'),
]