from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_tache, name='liste_tache'),
    path('ajouter/', views.ajouter_tache, name='ajouter_tache'),
    path('basculer/<int:id>/', views.basculer_tache, name='basculer_tache'),

]
