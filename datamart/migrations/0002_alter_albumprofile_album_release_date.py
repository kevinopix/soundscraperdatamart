# Generated by Django 4.1.3 on 2022-12-04 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumprofile',
            name='album_release_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]