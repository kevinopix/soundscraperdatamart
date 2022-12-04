from django.contrib import admin
from datamart.models import BandMember
from datamart.resources import BandMemberResource
from import_export.admin import ImportExportModelAdmin

class BandMemberAdmin(ImportExportModelAdmin):
    resource_classes = [BandMemberResource]


admin.site.register(BandMember, BandMemberAdmin)