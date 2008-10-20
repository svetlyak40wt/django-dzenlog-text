from django.contrib import admin
from models import TextPost
from django_dzenlog.admin import GeneralPostAdmin

admin.site.register(TextPost, GeneralPostAdmin)
