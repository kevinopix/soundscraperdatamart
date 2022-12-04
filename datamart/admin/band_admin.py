from django.contrib import admin
from datamart.models import Band
from datamart.resources import BandResource
from import_export.admin import ImportExportModelAdmin

class BandAdmin(ImportExportModelAdmin):
    resource_classes = [BandResource]


admin.site.register(Band, BandAdmin)