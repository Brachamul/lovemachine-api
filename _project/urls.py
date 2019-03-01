from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView

from android_apps.views import search_view

# Admin
admin.site.site_header = 'LoveMachine - Administration'


# URL Patterns

urlpatterns = [
	path('kissing-booth/', admin.site.urls, name='admin'),
	path('web/find_app/', search_view, name='play_store__app_search_web'),
	path('android_apps/', include('android_apps.urls'), name='android_apps'),
	path('android_users/', include('android_users.urls'), name='android_users'),
	path('reviews/', include('reviews.urls'), name='reviews'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)