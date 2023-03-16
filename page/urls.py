from django.contrib import admin
from django.urls import path
from spa.views import *
from django.contrib.auth.views import LoginView , LogoutView

urlpatterns = [
    path('', index, name='index'),
    path('service/', service, name='service'),
    path('admin/', admin.site.urls),
    path('custumer/', custumer, name='custumer'),
    path('tambah-custumer/', tambah_custumer, name='tambah-custumer'),
    path('custumer/ubah/<int:id_custumer>', ubah_custumer, name='ubah-custumer'),
    path('masuk/', LoginView.as_view(), name='masuk'),
    path('keluar/', LogoutView.as_view(next_page='masuk'), name='keluar'),
]
