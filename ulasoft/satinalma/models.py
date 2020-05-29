from django.db import models

class Siparisler(models.Model):
    sip_rec_no = models.IntegerField(unique=True)
    red_sayac = models.IntegerField()
    red_sebebi1 = models.TextField()
    red_sebebi2 = models.TextField()
    red_sebebi3 = models.TextField()
    red_sebebi4 = models.TextField()
    red_sebebi5 = models.TextField()
    cevap1 = models.TextField()
    cevap2 = models.TextField()
    cevap3 = models.TextField()
    cevap4 = models.TextField()
    cevap5 = models.TextField()
