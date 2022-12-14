# Generated by Django 4.1.3 on 2022-12-05 01:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Album Category',
                'verbose_name_plural': 'Album Categories',
            },
        ),
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('band_name', models.CharField(max_length=200)),
                ('country_origin', models.CharField(max_length=100)),
                ('year_formed', models.IntegerField()),
                ('soundcloud_band_url', models.URLField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BandAlbum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=200)),
                ('album_url', models.URLField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('band_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datamart.band')),
            ],
        ),
        migrations.CreateModel(
            name='SoundcloudAlbumSong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_URL', models.URLField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='datamart.bandalbum')),
            ],
        ),
        migrations.CreateModel(
            name='SoundcloudAlbumSongDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_title', models.CharField(max_length=300)),
                ('song_release_date', models.DateField()),
                ('song_plays', models.IntegerField()),
                ('song_likes', models.IntegerField()),
                ('song_reposts', models.IntegerField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('album_song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datamart.soundcloudalbumsong')),
            ],
            options={
                'verbose_name': 'Soundcloud Album Song Detail',
                'verbose_name_plural': 'Soundcloud Album Song Details',
            },
        ),
        migrations.CreateModel(
            name='BandProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followers', models.IntegerField()),
                ('following', models.IntegerField()),
                ('tracks', models.IntegerField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('band_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datamart.band')),
            ],
        ),
        migrations.CreateModel(
            name='BandMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=100)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('band_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datamart.band')),
            ],
        ),
        migrations.CreateModel(
            name='AlbumProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_likes', models.IntegerField()),
                ('album_reposts', models.IntegerField()),
                ('album_release_date', models.DateField(blank=True, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datamart.bandalbum')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datamart.albumcategory')),
            ],
        ),
    ]
