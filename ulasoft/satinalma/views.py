from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def satinalma(request):
    return render(request, 'satinalma.html')
