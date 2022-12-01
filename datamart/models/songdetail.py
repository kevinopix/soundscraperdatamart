from django.db import models
from datamart.models import SoundcloudAlbumSong


class SoundcloudAlbumSongDetail(models.Model):
    song_title = models.CharField(max_length=300)
    song_release_date = models.DateField()
    song_plays = models.IntegerField()
    song_likes = models.IntegerField()
    song_reposts = models.IntegerField()
    album_song = models.ForeignKey(SoundcloudAlbumSong, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.album_song.song_URL }"

    class Meta:
        verbose_name = "Soundcloud Album Song Detail"
        verbose_name_plural = "Soundcloud Album Song Details"

