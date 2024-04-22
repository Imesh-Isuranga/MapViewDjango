from django.db import models
import uuid

class Locations(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    latitude = models.FloatField(default=0.0)  # Provide a sensible default
    longitude = models.FloatField(default=0.0)  # Provide a sensible default

    def __str__(self):
        return f"Location: {self.latitude}, {self.longitude}"
