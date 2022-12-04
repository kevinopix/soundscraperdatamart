from django.db import models
from datamart.models import BandAlbum, AlbumCategory


class AlbumProfile(models.Model):
    album_likes = models.IntegerField()
    album_reposts = models.IntegerField()
    album_release_date = models.DateField(blank=True, null=True)
    album = models.ForeignKey(BandAlbum, on_delete=models.CASCADE)
    category = models.ForeignKey(AlbumCategory, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.album.album_name }"