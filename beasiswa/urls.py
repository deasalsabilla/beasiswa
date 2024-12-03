from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name='home'),
    path("kelola-angkatan/", views.angkatan, name='angkatan'),
    path("kelola-angkatan/tambah-angkatan/", views.tambah_angkatan, name='tambah_angkatan'),
    path("kelola-angkatan/edit-angkatan/<int:id>/", views.edit_angkatan, name='edit_angkatan'),
    path("kelola-angkatan/hapus-angkatan/<int:id>/", views.delete_angkatan, name='delete_angkatan'),
    path("kelola-mahasiswa/", views.mahasiswa, name='mahasiswa'),
]
