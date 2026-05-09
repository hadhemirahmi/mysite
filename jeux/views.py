
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Jeu
# pyrefly: ignore [missing-import]
from rest_framework import viewsets
# pyrefly: ignore [missing-import]
from .serializers import JeuSerializer
class JeuViewset(viewsets.ModelViewSet):
    queryset = Jeu.objects.all()
    serializer_class = JeuSerializer

 
class JeuListView(ListView):
    model = Jeu
    template_name = 'jeux/jeu_list.html'
    context_object_name = 'jeux'  

class JeuDetailView(DetailView):
    model = Jeu
    template_name = 'jeux/jeu_detail.html'
    context_object_name = 'jeu'  

class JeuCreateView(LoginRequiredMixin, CreateView):
    model = Jeu
    template_name = 'jeux/jeu_form.html'
    fields = '__all__'
    success_url = '/jeux/'

class JeuUpdateView(LoginRequiredMixin, UpdateView):
    model = Jeu
    template_name = 'jeux/jeu_form.html'
    fields = '__all__'
    success_url = '/jeux/'

class JeuDeleteView(LoginRequiredMixin, DeleteView):
    model = Jeu
    template_name = 'jeux/jeu_confirm_delete.html'
    success_url = '/jeux/'
