from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def accueil(request):
    return render(request, 'accueil.html')

def logout_view(request):
    logout(request)
    return redirect('accueil')  
