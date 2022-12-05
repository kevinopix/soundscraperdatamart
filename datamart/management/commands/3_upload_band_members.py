import pandas as pd
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from datamart.models import Band, BandMember

class Command(BaseCommand):

    def handle(self, *args, **options):
        to_import = pd.read_csv('df_band_members.csv', encoding='cp1252')
        to_import.columns = ['soundcloud_band_url','first_name', 'last_name']
        # print(to_import)
        exist = pd.DataFrame(Band.objects.values('pk','soundcloud_band_url'))
        joined = pd.merge(exist, to_import, on='soundcloud_band_url', how='left')
        joined.columns = ['band_pk','soundcloud_band_url','first_name', 'last_name']
        # print(joined)
        # print(len(joined))
        for index, row in joined.iterrows():
            band_pk_val = row['band_pk']
            first_name_val = row['first_name']
            last_name_val = row['last_name']
            try:
                val_exist = BandMember.objects.get(
                    band_name=Band(pk=band_pk_val),
                    first_name=first_name_val,
                    last_name=last_name_val
                )
            except ObjectDoesNotExist:
                val_exist = None
                model = BandMember()
                model.first_name = first_name_val
                model.last_name = last_name_val
                model.band_name = Band(pk=band_pk_val)
                model.save()
            # print(band_pk_val, first_name_val, last_name_val, val_exist)
