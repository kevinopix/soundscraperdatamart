import pandas as pd
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from datamart.models import SoundcloudAlbumSong, SoundcloudAlbumSongDetail


class Command(BaseCommand):

    def handle(self, *args, **options):
        to_import = pd.read_csv('df_songs_detail_all_prod.csv')
        to_import = to_import.drop(columns=['Unnamed: 0'])
        # print(to_import)
        songs = pd.DataFrame(SoundcloudAlbumSong.objects.values('pk','song_URL'))
        songs.columns = ['song_pk', 'song_link']

        fin = pd.merge(to_import, songs, on=['song_link'], how='left')
        fin['song_release_date'] = pd.to_datetime(fin['song_release_date'])
        for index, row in fin.iterrows():
            song_pk_val = row['song_pk']
            try:
                val_exist = SoundcloudAlbumSongDetail.objects.get(
                    album_song=SoundcloudAlbumSong(pk=song_pk_val)
                )
            except ObjectDoesNotExist:
                model = SoundcloudAlbumSongDetail()
                model.album_song = SoundcloudAlbumSong(pk=song_pk_val)
                model.song_title = row['song_title']
                model.song_plays = row['song_plays']
                model.song_likes = row['song_likes']
                model.song_reposts = row['song_reposts']
                model.song_release_date = row['song_release_date']
                model.save()
