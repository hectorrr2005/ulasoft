from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    mikroUserId = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'


class Donem(models.Model):
    donem = models.DateField()


class Mutabakat(models.Model):
    donem = models.ForeignKey(Donem, on_delete=models.CASCADE)
    kayit_tarihi = models.DateTimeField(auto_now_add=True)
    cari_unvan = models.CharField(max_length=300)
    vergi_kimlik_no = models.CharField(max_length=11)
    ulke_kodu = models.CharField(max_length=5)
    email = models.EmailField()
    bs_belge_sayisi = models.IntegerField()
    bs_toplam_tutar = models.FloatField()
    ba_belge_sayisi = models.IntegerField()
    ba_toplam_tutar = models.FloatField()


