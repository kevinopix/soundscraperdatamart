from django.db import models

class SoundcloudAlbumSong(models.Model):
    song_URL = models.URLField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.song_URL }"