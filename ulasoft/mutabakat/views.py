from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'index.html')

@login_required
def profile(request):
    return render(request, 'profile.html')