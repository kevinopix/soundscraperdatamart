from django.db import models
from datamart.models import BandAlbum

class SoundcloudAlbumSong(models.Model):
    song_URL = models.URLField()
    album = models.ForeignKey(BandAlbum, on_delete=models.DO_NOTHING)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.song_URL }"