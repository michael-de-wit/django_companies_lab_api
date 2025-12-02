from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=64)
    industry = models.CharField(max_length=64)
    location = models.ForeignKey(
        'locations_api.Location',
        on_delete=models.CASCADE,
        db_column='location_id',
        to_field='id',
        null=True,
        blank=True
    )
