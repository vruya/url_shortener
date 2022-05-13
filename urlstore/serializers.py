
from dataclasses import fields
from rest_framework import serializers
from .models import UrlStore


class UrlStoreSerializer(serializers.ModelSerializer):
    short_url = serializers.SerializerMethodField()

    class Meta:
        model = UrlStore
        fields = ('url', 'short_url')

    def get_short_url(self, obj):
        return str(obj.pk)

    @staticmethod
    def increase_visit(instance):
        instance.visit_counter += 1
        instance.save()
