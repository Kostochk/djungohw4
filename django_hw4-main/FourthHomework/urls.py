from django.urls import path
from . import views

urlpatterns = [
    path('', views.song_view, name='song_en'),
    path('fr/', views.song_view, {'lang': 'fr'}),
    path('de/', views.song_view, {'lang': 'de'}),
    path('es/', views.song_view, {'lang': 'es'}),
    
    path('cars/', views.cars_view),
    path('cars/<str:brand>/', views.cars_view),
    
    path('today/', views.day_view),
    
    path('headphones/', views.headphones_view), ]