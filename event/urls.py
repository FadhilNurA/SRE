from django.urls import path
from . import views

app_name = 'event'

urlpatterns = [
    path('pentahelix-talks/', views.pentahelix, name='pentahelix-talks'),  # tambahkan slash di akhir
    path('workshop/', views.workshop, name='workshop'),
    path('field-trip/', views.field_trip, name='field-trip'),
]
