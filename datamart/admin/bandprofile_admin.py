from django.contrib import admin
from datamart.models import BandProfile
from datamart.resources import BandProfileResource
from import_export.admin import ImportExportModelAdmin

class BandProfileAdmin(ImportExportModelAdmin):
    resource_classes = [BandProfileResource]


admin.site.register(BandProfile, BandProfileAdmin)