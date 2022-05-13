from django.http import HttpResponseRedirect
from rest_framework import generics, views
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from .serializers import UrlStoreSerializer
from .models import UrlStore


class UrlStoreViewSet(
    CreateModelMixin,
    RetrieveModelMixin,
    GenericViewSet
):
    queryset = UrlStore.objects.all()
    serializer_class = UrlStoreSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        serializer.increase_visit(instance)
        data = serializer.data
        return HttpResponseRedirect(data['url'])
