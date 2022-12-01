from django.db import models
from datamart.models import Band


class BandAlbum(models.Model):
    album_name = models.CharField(max_length=200)
    album_url = models.URLField()
    band_name = models.ForeignKey(Band, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.band_name.band_name } --- {self.album_name}"