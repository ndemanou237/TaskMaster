from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# from tasks.forms import TacheForm
from .models import Tache
from .forms import TacheForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

#affiche la liste des taches d'un utilisateur precis connecté en ordre du plus recent au plus ancien
@login_required
def liste_tache(request):
    taches = Tache.objects.filter(utilisateur=request.user).order_by('date_echeance')
    context = {
        'taches':taches
    }
    return render(request, 'tasks/dashboard.html', context)

#faire quitter une tache a terminé dde l'utilisateur connecté et le redirige vers le liste des taches
@login_required
def basculer_tache(request, id):
    tache = get_object_or_404(Tache, id=id, utilisateur = request.user)
    tache.marquer_comme_terminee()
    return redirect('liste_taches')

#simple formulaire pour l'ajout d'une tache si c'est en method post et renvoie un formulaire vie si c'est une autre methode
@login_required
def ajouter_tache(request):
    if request.method == 'POST':
        form = TacheForm(request.POST)
        if form.is_valid():
            tache = form.save(commit=False)
            tache.utilisateur = request.user 
            tache.save()
            return redirect('liste_taches')
    else:
        form = TacheForm()

    context = {
        'form': form
    }

    return render(request, 'tasks/ajouter.html', context)

def connexion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('liste_taches')
    else:
        form = AuthenticationForm()
        context = {
            'form':form
        }    
    return render(request, 'tasks/connexion.html', context)    
    
def deconnexion(request):
    logout(request)
    return redirect('connexion')    