import pandas as pd
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from datamart.models import Band

class Command(BaseCommand):

    def handle(self, *args, **options):
        to_import = pd.read_csv('Band-2022-12-05.csv', encoding='cp1252')
        to_import = to_import[['band_name', 'country_origin', 'year_formed', 'soundcloud_band_url']]
        # to_import.columns = ['soundcloud_band_url','followers', 'following', 'tracks']
        # print(to_import)

        for index, row in to_import.iterrows():
            band_url = row['soundcloud_band_url']
            try:
                val_exist = Band.objects.get(
                    soundcloud_band_url=band_url
                )
            except ObjectDoesNotExist:
                val_exist = None
                model = Band()
                model.band_name = row['band_name']
                model.country_origin = row['country_origin']
                model.year_formed = row['year_formed']
                model.soundcloud_band_url = row['soundcloud_band_url']
                model.save()
        #     print(band_pk_val, first_name_val, last_name_val, val_exist)
