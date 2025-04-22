from django.urls import path
from . import views

app_name = 'compe'

urlpatterns = [
    path('bcc/', views.compe_bcc, name='bcc'),  # tambahkan slash di akhir
    path('pcc/', views.compe_pcc, name='pcc'),
    path('reic/', views.compe_reic, name='reic'),
]
