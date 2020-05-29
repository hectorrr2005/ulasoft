from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .mssqlconn import satinalmaOnaysizGetir, satinalmaOnayliGetir, satinalmaOnayla, satinalmaOnayIptal, satinalmaReddedilenGetir
from mutabakat.models import Profile


@login_required
def satinalma(request):    
    data = satinalmaOnaysizGetir()
    context = {
        "data": data,
    }
    return render(request, 'satinalma.html', context)

@login_required
def satinalmaOnayli(request):
    data = satinalmaOnayliGetir()
    context = {
        "data": data,
    }
    return render(request, 'satinalmaOnayli.html', context)

@login_required
def satinalmReddedilen(request):
    data = satinalmaReddedilenGetir()
    context = {
        "data": data,
    }
    return render(request, 'satinalmaReddedilen.html', context)

@login_required
def onayla(request, id):
    profil = Profile.objects.filter(user = request.user)    
    satinalmaOnayla(id, profil[0].mikroUserId)
    data = satinalmaOnaysizGetir()
    context = {
        "data": data,
    }
    return render(request, 'satinalma.html', context)

@login_required
def onayiptal(request, id):
    satinalmaOnayIptal(id)
    data = satinalmaOnayliGetir()
    context = {
        "data": data,
    }
    return render(request, 'satinalmaOnayli.html', context)