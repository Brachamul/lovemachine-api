from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView

from play_store.views import search_view

# Admin
admin.site.site_header = 'LoveMachine - Administration'


# URL Patterns

urlpatterns = [
	path('kissing-booth/', admin.site.urls, name='admin'),
	path('search/', search_view, name='play_store__search')
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# REST Framework

from rest_framework import routers
from play_store import views

router = routers.DefaultRouter()
router.register(r'apps', views.AppViewSet)

urlpatterns += [
    path('', include(router.urls)),
	path('api-auth/', include('rest_framework.urls'))
]