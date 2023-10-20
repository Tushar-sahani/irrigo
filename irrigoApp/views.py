from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Detail
# Create your views here.
def index(request):
    if request.method == 'POST':
        first_Name = request.POST['first_Name']
        last_Name= request.POST['last_Name']
        phone_Number= request.POST['phone_Number']
        adhar_Number= request.POST['adhar_Number']
        rfid= request.POST['rfid']
        Detail.objects.create(first_Name=first_Name,last_Name=last_Name,phone_Number=phone_Number,adhar_Number=adhar_Number,rfid=rfid).save()
        messages.success(request,"Your Registration Successfull")

    return render(request,'index.html') 