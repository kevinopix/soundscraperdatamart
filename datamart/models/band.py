from django.db import models


class Band(models.Model):
    band_name = models.CharField(max_length=200)
    country_origin = models.CharField(max_length=100)
    year_formed = models.IntegerField()
    soundcloud_band_url = models.URLField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.band_name}"
