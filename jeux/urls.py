from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('jeu-api', views.JeuViewset, basename='jeu-api')

urlpatterns = [
    path('', views.JeuListView.as_view(), name='jeu_list'),
    path('<int:pk>/', views.JeuDetailView.as_view(), name='jeu_detail'),
    path('create/', views.JeuCreateView.as_view(), name='jeu_create'),
    path('<int:pk>/update/', views.JeuUpdateView.as_view(), name='jeu_update'),
    path('<int:pk>/delete/', views.JeuDeleteView.as_view(), name='jeu_delete'),
    path('api/', include(router.urls)), # API accessible sur /jeux/api/
]
