from django.contrib import admin
from .models import Angkatan, Prodi, Mahasiswa
admin.site.site_header = 'SIPB'
admin.site.register(Angkatan)
admin.site.register(Prodi)
admin.site.register(Mahasiswa)