

from django.contrib import admin
from django.urls import path, include
from urlstore.views import UrlStoreViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'u', UrlStoreViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
