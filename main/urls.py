from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'sre' 

urlpatterns = [
    path('', views.sre_home, name='sre_home'),
    # path('success/', views.success, name='success'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)