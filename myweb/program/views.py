from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def berita(request):
    template = loader.get_template('berita.html')
    return HttpResponse(template.render())
def detailberita(request):
    template = loader.get_template('detailberita.html')
    return HttpResponse(template.render())

# Create your views here.
