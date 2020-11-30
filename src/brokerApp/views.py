
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .filters import *
from django.core.mail import send_mail




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

def apartmentDetail(request,pk):

    property_data = Property.objects.filter(renting="no")
    if request.method == "POST":
        name   = request.POST.get('name')
        email  = request.POST.get('email')
        phone  = request.POST.get('phone')
        number = request.POST.get('number')
        
        #sending mail
        # send_mail(
          #'Nowy klient realestate', #subject
          #'Imie i nazwisko klienta:' + values["name"] + values['surname'] + " numer telefontu " + values['phone'] + "email klienta" + values['email'],#content
          #values['email'],#from who 
          #['wwenergywebsite@gmail.com']#)

    context={
        'data':property_data
    }
    return render(request,'detailView.html', context)