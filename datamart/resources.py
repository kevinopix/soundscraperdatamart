from import_export import resources
from datamart.models import Band, BandProfile, BandMember

class BandResource(resources.ModelResource):

    class Meta:
        model = Band


class BandProfileResource(resources.ModelResource):

    class Meta:
        model = BandProfile


class BandMemberResource(resources.ModelResource):

    class Meta:
        model = BandMember