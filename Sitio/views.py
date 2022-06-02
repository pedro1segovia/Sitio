from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy

def menu_principal(request):
     return render(request, 'menu/index.html')

def login(request):
     return render(request, 'menu/login.html')



