from django.db import models

class berita(models.Model):
  namaberita = models.CharField(max_length=255)
  tanggal    = models.DateField(null=True)
  
  def __str__(self):
    return f"{self.namaberita} {self.tanggal}"