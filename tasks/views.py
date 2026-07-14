from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tache

@login_required
def liste_tache(request):
    taches = Tache.objects.filter(utilisateur=request.user).order_by('date_echeance')
    context = {
        'taches':taches
    }
    return render(request, 'task/dashboard.html', context)

@login_required
def basculer_tache(request, id):
    tache = get_object_or_404(Tache, id=id, utilisateur = request.user)
    tache.marquer_comme_terminee()
    return redirect('liste_taches')

@login_required
def ajouter_tache(request):
    if request.method == 'POST':
        pass
    return render(request, 'task/ajouter.html')