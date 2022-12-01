from django.db import models
from datamart.models import Band

class BandProfile(models.Model):
    followers = models.IntegerField()
    following = models.IntegerField()
    tracks = models.IntegerField()
    band_name = models.ForeignKey(Band, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.band_name.band_name }"