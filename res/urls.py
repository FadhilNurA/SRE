# res/urls.py

from django.urls import path
from . import views

app_name = 'res'  # <-- ini WAJIB untuk namespace

urlpatterns = [
    path('', views.res_home, name='home'),
]
