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
