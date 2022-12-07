from django.shortcuts import render
from django.views import generic
from django.middleware.csrf import rotate_token
from datamart.models import Band
from django.db import connection
import pandas as pd
import json


class HomeView(generic.DetailView):
    template_name = "home/home.html"
    # model = Band

    def get(self, *args, **kwargs):
        rotate_token(self.request)
        context = {}
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(DISTINCT soundcloud_band_url) FROM datamart_band")
            val1 = cursor.fetchone()
            cursor.execute("SELECT COUNT(DISTINCT id) FROM datamart_bandmember")
            val2 = cursor.fetchone()
            cursor.execute("SELECT COUNT(DISTINCT id) FROM datamart_albumcategory")
            val3 = cursor.fetchone()
            cursor.execute("SELECT COUNT(DISTINCT id) FROM datamart_bandalbum")
            val4 = cursor.fetchone()
            cursor.execute("SELECT COUNT(DISTINCT id) FROM datamart_soundcloudalbumsong")
            val5 = cursor.fetchone()
            cursor.execute("""
                SELECT DISTINCT bb.category_name, COUNT(aa.album_id) AS count_albums
                FROM datamart_albumprofile aa
                LEFT JOIN datamart_albumcategory bb ON bb.id = aa.category_id
                GROUP BY bb.category_name
                ORDER BY COUNT(aa.album_id) DESC
            """)
            val6 = cursor.fetchall()

        # print(val6)
        albums_dist = pd.DataFrame(val6)
        albums_dist.columns = ['category_name', 'count_albums']
        albums_dist_json_records = albums_dist.reset_index().to_json(orient='records')
        albums_dist_data = []
        albums_dist_data = json.loads(albums_dist_json_records)
        band_count = val1[0]
        band_member_count = val2[0]
        album_categories_count = val3[0]
        band_album_count = val4[0]
        tracks_count = val5[0]
        context['band_count'] = band_count
        context['band_member_count'] = band_member_count
        context['album_categories_count'] = album_categories_count
        context['band_album_count'] = band_album_count
        context['tracks_count'] = tracks_count
        context['album_distro'] = albums_dist_data
        return render(self.request, self.template_name, context)
