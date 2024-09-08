from django.shortcuts import render
from django.http import HttpResponse
from Forum.models import *

# Create your views here.

def home(request):
    return render(request, 'home.html')

def perfil_view(request):
    comentarios = Comentario.objects.filter(autor_id=request.user.id)
    return render(request, 'Account/perfil.html', {'comentarios': comentarios})

