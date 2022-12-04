import pandas as pd
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from datamart.models import BandAlbum, AlbumCategory


class Command(BaseCommand):

    def handle(self, *args, **options):
        to_import = pd.read_csv('df_album_details_all.csv')
        # to_import = to_import.drop(columns=['Unnamed: 0'])
        # print(to_import)
        categories = to_import['album_category'].unique().tolist()
        print(categories)
        df_cat = pd.DataFrame()
        df_cat['category_name'] = categories
        exist = pd.DataFrame(AlbumCategory.objects.values('pk', 'category_name'))
        # exist.columns = ['album_pk', 'category_name']
        print(exist)
        for index, row in df_cat.iterrows():
            val = row['category_name']
            try:
                val_exist = AlbumCategory.objects.get(
                    category_name=val
                )
            except ObjectDoesNotExist:
                val_exist = None
                model = AlbumCategory()
                model.category_name = val
                model.save()