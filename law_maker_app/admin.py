from django.contrib import admin

from law_maker_app.models import Config, Initiative, Initiator, Committee, Petition, \
    PetitionSignature

admin.register(Config)
admin.register(Initiative)
admin.register(Initiator)
admin.register(Committee)
admin.register(Petition)
admin.register(PetitionSignature)
