
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .filters import *




def home(request):


    context={}
    return render(request,'home.html', context)

def apartments(request):
    property_data = Property.objects.all()
    myFilter = PropertyFilter()
    if request.method == 'GET':
        filtera = PropertyFilter(request.GET, queryset=property_data)
        property_data = filtera.qs

    context={
        'myFilter':myFilter,
        'data':property_data
    }
    return render(request,'broker.html', context)