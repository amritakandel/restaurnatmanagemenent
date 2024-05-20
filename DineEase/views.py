from django.http import HttpResponse
from django.shortcuts import render
from reservation.models import Reservation
def homePage(request):
   
   return render(request, "index.html")

def aboutUsPage(request):
   
   return render(request, "aboutus.html")
def loginPage(request):
    return render(request, "loginn.html")

def signupPage(request):
    return render(request, "signupp.html")

def reservationPage(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        date=request.POST.get('date')
        time=request.POST.get('time')
        guests=request.POST.get('guests')
        r=Reservation(Name=name,Email=email,Phone=phone,Date=date,Time=time,Guest=guests)
        r.save()

    


    return render(request, "reservation.html")


