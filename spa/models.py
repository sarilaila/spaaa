from django.db import models


class Kategori(models.Model):
    kategori = models.CharField(max_length=50)

    def __str__(self):
        return self.kategori


class Custumer(models.Model):
    nama = models.CharField(max_length=50)
    no_hp = models.IntegerField(max_length=13, null=True)
    alamat = models.CharField(max_length=50)
    tgl = models.CharField(max_length=50)
    keterangan = models.CharField(max_length=50)
    kategori = models.ForeignKey(
        Kategori, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nama
