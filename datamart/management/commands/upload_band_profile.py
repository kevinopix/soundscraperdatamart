import pandas as pd
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from datamart.models import Band, BandProfile

class Command(BaseCommand):

    def handle(self, *args, **options):
        to_import = pd.read_csv('df_band_prod.csv')
        to_import = to_import[['Band_URL','followers', 'following', 'tracks']]
        to_import.columns = ['soundcloud_band_url','followers', 'following', 'tracks']
        exist = pd.DataFrame(Band.objects.values('pk','soundcloud_band_url'))
        joined = pd.merge(exist, to_import, on='soundcloud_band_url', how='left')
        joined.columns = ['band_pk','soundcloud_band_url','followers', 'following', 'tracks']
        print(joined)
        for index, row in joined.iterrows():
            band_pk_val = row['band_pk']
            try:
                val_exist = BandProfile.objects.get(band_name=Band(pk=band_pk_val))
            except ObjectDoesNotExist:
                val_exist = None
                followers_val = row['followers']
                following_val = row['following']
                tracks_val = row['tracks']
                model = BandProfile()
                model.followers = followers_val
                model.following = following_val
                model.tracks = tracks_val
                model.band_name = Band(pk=band_pk_val)
                model.save()
