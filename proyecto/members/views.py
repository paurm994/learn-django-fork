from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return render(request, "index.html")

def members(request):
  # Devolvemos HTML por archivo:
  return render(request, "members/index.html")
