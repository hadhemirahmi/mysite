from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name='index'),
 path('majProduits/', views.P_index, name='majProduits'),
 path('vitrine/', views.vitrine, name='vitrine'),
path('nouveauFournisseur/', views.nouveauFournisseur, name='nouveauFournisseur'),
path('register/',views.register, name = 'register'),
path('logout/',views.logout, name = 'logout'),

 ]
