import uuid

from django.db import models


class UrlStore(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.TextField()
    visit_counter = models.IntegerField(default=0)
