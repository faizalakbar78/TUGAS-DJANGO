from django.urls import path
from . import views

urlpatterns = [
    path('berita', views.berita, name='berita'),
    path('detailberita', views.detailberita, name='detailberita'),
]
