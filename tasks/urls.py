from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_tache, name='liste_taches'),
    path('ajouter/', views.ajouter_tache, name='ajouter_tache'),
    path('basculer/<int:id>/', views.basculer_tache, name='basculer_tache'),
    path('login/', views.connexion, name='connexion'),
    path('logout/', views.deconnexion, name='deconnexion'),

]
