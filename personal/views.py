from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse, request

def home(request):
    return render(request, 'home.html')