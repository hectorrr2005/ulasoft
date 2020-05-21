from django.urls import path
from .views import satinalma


urlpatterns = [
    path('', satinalma, name='satinalma'),
]
