from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('india/', views.india, name="india"),
    path('bollywood/', views.bollywood, name="bollywood"),
    path('sport/', views.sport, name="sport"),
    path('health/', views.health, name="health"),
    path('details/<int:id>', views.details, name="details"),
    path('search/', views.search, name="search"),
    
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
