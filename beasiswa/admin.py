from django.contrib import admin
from .models import Angkatan, Prodi
admin.site.site_header = 'SIPB'
admin.site.register(Angkatan)
admin.site.register(Prodi)