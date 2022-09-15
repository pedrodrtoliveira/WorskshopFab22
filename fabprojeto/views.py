from urllib import response
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def pagina1 (request):
    
    return render(request, template_name='fabprojeto/index.html')