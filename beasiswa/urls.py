from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name='home'),
    path("kelola-angkatan/", views.angkatan, name='angkatan'),
    path("kelola-angkatan/tambah/", views.tambah_angkatan, name='tambah_angkatan'),
    path("kelola-angkatan/edit/<int:id>/", views.edit_angkatan, name='edit_angkatan'),
    path("kelola-angkatan/hapus/<int:id>/", views.delete_angkatan, name='delete_angkatan'),
    path("kelola-prodi/", views.prodi, name='prodi'),
    path("kelola-prodi/tambah/", views.tambah_prodi, name='tambah_prodi'),
    path("kelola-prodi/edit/<int:id>/", views.edit_prodi, name="edit_prodi"),
    path("kelola-prodi/hapus/<int:id>/", views.hapus_prodi, name="hapus_prodi"),
    path("kelola-mahasiswa/", views.mahasiswa, name='mahasiswa'),
    path("kelola-mahasiswa/tambah", views.tambah_mahasiswa, name='tambah_mahasiswa'),
    path('mahasiswa/edit/<int:id>/', views.edit_mahasiswa, name='edit_mahasiswa'),
]
