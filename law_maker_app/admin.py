from django.contrib import admin
from django.contrib.admin import AdminSite

from law_maker_app.models import Config, Initiative, Initiator, Committee, Petition, \
    PetitionSignature


class MyAdminSite(AdminSite):
    site_title = 'Hello there'
    site_header = 'Hello there2'


admin.site.register(Config)
admin.site.register(Initiative)
admin.site.register(Initiator)
admin.site.register(Committee)
admin.site.register(Petition)
admin.site.register(PetitionSignature)
