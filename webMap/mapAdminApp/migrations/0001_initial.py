# Generated by Django 4.2.11 on 2024-04-22 13:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Locations",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("latitude", models.FloatField(default=0.0)),
                ("longitude", models.FloatField(default=0.0)),
            ],
        ),
    ]
