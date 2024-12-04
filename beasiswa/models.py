from django.db import models

class Angkatan(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-increment ID
    angkatan = models.PositiveIntegerField(unique=True)  # Tahun angkatan, harus unik

    def __str__(self):
        return str(self.angkatan)

    class Meta:
        verbose_name = "Angkatan"
        verbose_name_plural = "Angkatan"
        ordering = ["angkatan"]  # Mengurutkan berdasarkan tahun angkatan
        
class Prodi(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-increment ID
    prodi = models.CharField(max_length=25)

    def __str__(self):
        return str(self.prodi)

    class Meta:
        verbose_name = "Prodi"
        verbose_name_plural = "Prodi"
        ordering = ["id"]

class Mahasiswa(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-increment ID
    nim = models.CharField(max_length=8, unique=True)  # NIM harus unik
    nama = models.CharField(max_length=100)  # Nama mahasiswa
    prodi = models.ForeignKey(Prodi, on_delete=models.CASCADE, related_name="mahasiswa")  # Relasi ke Prodi
    angkatan = models.ForeignKey(Angkatan, on_delete=models.CASCADE, related_name="mahasiswa")  # Relasi ke Angkatan

    def __str__(self):
        return f"{self.nim} - {self.nama}"

    class Meta:
        verbose_name = "Mahasiswa"
        verbose_name_plural = "Mahasiswa"
        ordering = ["nim"]  # Mengurutkan berdasarkan NIM