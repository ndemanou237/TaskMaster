from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Categorie(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Tache(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    date_echeance = models.DateTimeField()
    est_termine = models.BooleanField(default=False)

    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.titre
    
    def marquer_comme_terminee(self):
        self.est_termine = True
        self.save()

    def est_en_retard(self):
        return timezone.now () > self.date_echeance and not self.est_termine   
