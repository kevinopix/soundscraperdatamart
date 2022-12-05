import pandas as pd
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from datamart.models import BandAlbum, AlbumCategory, AlbumProfile


class Command(BaseCommand):

    def handle(self, *args, **options):
        to_import = pd.read_csv('df_album_details_all.csv')
        to_import[['album_likes','album_reposts']] = to_import[['album_likes','album_reposts']].fillna(0)#.astype(int)
        # to_import = to_import.drop(columns=['Unnamed: 0'])
        # to_import['album_likes'] = to_import['album_likes'].map(lambda x: int(x.replace(',','')))
        # print(to_import)
        cats = pd.DataFrame(AlbumCategory.objects.values('pk', 'category_name'))
        cats.columns = ['cat_pk', 'album_category']
        # print(cats)
        albs = pd.DataFrame(BandAlbum.objects.values('pk', 'album_url'))
        albs.columns = ['album_pk','album_link']
        # print(albs)

        new1 = pd.merge(to_import, cats, on=['album_category'], how='left')
        new1 = new1.drop(columns='album_category')
        # print(new1)

        new2 = pd.merge(new1, albs, on=['album_link'], how='left')
        new2['album_release_date'] = pd.to_datetime(new2['album_release_date'])
        # print(new2)

        # print(new2[new2['album_release_date'].isnull()])

        for index, row in new2.iterrows():
            # print(row)
            album_pk_val = row['album_pk']
            category_pk_val = row['cat_pk']
            try:
                val_exist = AlbumProfile.objects.get(
                    album=BandAlbum(pk=album_pk_val)
                )
            except ObjectDoesNotExist:
                val_exist = None
                album_likes_val = row['album_likes']
                album_reposts_val = row['album_reposts']
                album_release_date_val = row['album_release_date']
                model = AlbumProfile()
                model.album = BandAlbum(pk=album_pk_val)
                model.category = AlbumCategory(pk=category_pk_val)
                model.album_likes = album_likes_val
                model.album_reposts = album_reposts_val
                model.album_release_date = album_release_date_val
                model.save()
