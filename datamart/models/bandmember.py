from django.db import models
from datamart.models import Band


class BandMember(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=100)
    band_name = models.ForeignKey(Band, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.band_name.band_name } --- {self.first_name} --- {self.last_name}"