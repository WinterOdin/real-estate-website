
from django.shortcuts import render, redirect
from django.http import HttpResponse




def home(request):


    context={}
    return render(request,'home.html', context)

def apartments(request):


    context={}
    return render(request,'broker.html', context)