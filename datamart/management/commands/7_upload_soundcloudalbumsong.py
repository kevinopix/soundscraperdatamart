import pandas as pd
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from datamart.models import BandAlbum, AlbumCategory, AlbumProfile, SoundcloudAlbumSong


class Command(BaseCommand):

    def handle(self, *args, **options):
        to_import = pd.read_csv('df_album_songs_all.csv')
        to_import.columns = ['album_url', 'song_link']
        exist = pd.DataFrame(BandAlbum.objects.values('pk', 'album_url'))
        fin = pd.merge(to_import, exist, on=['album_url'], how='left')
        fin.columns = ['album_url', 'song_link', 'album_pk']
        # print(fin)
        for index, row in fin.iterrows():
            # print(row)
            # album_link_val = row['album_url']
            album_pk_val = row['album_pk']
            song_link_val = row['song_link']
            try:
                val_exist = SoundcloudAlbumSong.objects.get(
                    song_URL=song_link_val,
                    album=BandAlbum(pk=album_pk_val)
                )
            except ObjectDoesNotExist:
                model = SoundcloudAlbumSong()
                model.album = BandAlbum(pk=album_pk_val)
                model.song_URL = song_link_val
                model.save()
