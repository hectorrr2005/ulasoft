from django.urls import path
from .views import home, profile
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('login', LoginView.as_view(template_name='login.html'), name='login' ),
    path('', home, name='home'),
    path('profile/', profile, name='profile'),
]
