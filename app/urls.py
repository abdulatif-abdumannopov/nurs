from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('service/', service, name='service'),
    path('account/', account, name='account'),
    path('login/', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),
    path('registration/', registration, name='registration'),
]