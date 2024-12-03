from django.contrib import admin
from .models import Angkatan
admin.site.site_header = 'SIPB'
admin.site.register(Angkatan)