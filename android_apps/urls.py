from django.urls import include, path

from . import calls



urlpatterns = [
	path('find/', calls.find, name='android_apps__find'),
]