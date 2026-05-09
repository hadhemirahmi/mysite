from urllib import request
from .forms import ProduitForm, FournisseurForm, UserRegistrationForm
from django.contrib.auth import login, authenticate, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from .models import Produit, Categorie, Fournisseur


def index(request):
    categories = Categorie.objects.all()

    categorie_id = request.GET.get('categorie')
    if categorie_id:
        products = Produit.objects.filter(categorie_id=categorie_id)
    else:
        products = Produit.objects.all()

    context = {
        'products': products,
        'categories': categories,
        'selected_category': int(categorie_id) if categorie_id else None
    }
    return render(request, 'magasin/mesProduits.html', context)


@login_required
def P_index(request):
    if request.method == "POST":
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProduitForm()
    categories = Categorie.objects.all()
    return render(request, 'magasin/majProduits.html', {'form': form, 'categories': categories})


def vitrine(request):
    list = Produit.objects.all()
    categories = Categorie.objects.all()
    return render(request, 'magasin/vitrine.html', {'list': list, 'categories': categories})


@login_required
def nouveauFournisseur(request):
    if request.method == "POST":
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nouveauFournisseur')
    else:
        form = FournisseurForm()

    liste_fournisseurs = Fournisseur.objects.all()
    categories = Categorie.objects.all()

    context = {
        'form': form,
        'liste_fournisseurs': liste_fournisseurs,
        'categories': categories
    }

    return render(request, 'magasin/fournisseur.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)

            messages.success(request, f'Coucou {username}, votre compte a été créé avec succès !')
            return redirect('accueil')   
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


def logout(request):
    auth_logout(request)  
    return redirect('login')   


def reniouveler_mot_de_passe(request):
    return render(request, 'registration/password_reset.html')

