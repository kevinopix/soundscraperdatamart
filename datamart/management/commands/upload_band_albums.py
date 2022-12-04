import pandas as pd
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from datamart.models import Band, BandAlbum


class Command(BaseCommand):

    def handle(self, *args, **options):
        to_import = pd.read_csv('df_albums_all_prod.csv')
        to_import = to_import.drop(columns=['Unnamed: 0'])
        # print(to_import)
        exist = pd.DataFrame(Band.objects.values('pk', 'soundcloud_band_url'))
        exist.columns = ['pk', 'band_URL']
        joined = pd.merge(exist, to_import, on='band_URL', how='left')
        joined.columns = ['band_pk', 'band_URL', 'album_name', 'album_url']
        # print(joined)
        for index, row in joined.iterrows():
            band_pk_val = row['band_pk']
            album_url_val = row['album_url']
            album_name_val = row['album_name']
            try:
                val_exist = BandAlbum.objects.get(
                    band_name=Band(pk=band_pk_val),
                    album_url=album_url_val
                )
            except ObjectDoesNotExist:
                val_exist = None
                model = BandAlbum()
                model.album_name = album_name_val
                model.album_url = album_url_val
                model.band_name = Band(pk=band_pk_val)
                model.save()
            print(band_pk_val, album_url_val, album_name_val, val_exist)