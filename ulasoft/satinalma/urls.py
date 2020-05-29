from django.urls import path
from .views import satinalma, satinalmaOnayli, onayla, onayiptal, satinalmReddedilen


urlpatterns = [
    path('', satinalma, name='satinalma'),
    path('onayli/', satinalmaOnayli, name='satinalmaOnayli'),
    path('reddedilen/', satinalmReddedilen, name='satinalmaReddedilen'),
    path('onayla/<int:id>', onayla, name='onayla'),
    path('onayiptal/<int:id>', onayiptal, name='onayiptal'),
]
