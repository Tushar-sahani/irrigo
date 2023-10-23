from django.shortcuts import render,redirect
from django.contrib import messages
from django.db import IntegrityError
from .models import Detail
from .forms import DetailForms
# Create your views here.
# def index(request):
#     if request.method == 'POST':
#         first_Name = request.POST['first_Name']
#         last_Name= request.POST['last_Name']
#         phone_Number= request.POST['phone_Number']
#         adhar_Number= request.POST['adhar_Number']
#         rfid= request.POST['rfid']
#         Detail.objects.create(first_Name=first_Name,last_Name=last_Name,phone_Number=phone_Number,adhar_Number=adhar_Number,rfid=rfid).save()
#         messages.success(request,"Your Registration Successfull")

#     return render(request,'index.html')

def index(request):
    if request.method == 'POST':
        form = DetailForms(request.POST)
        if form.is_valid():
            adhar_number = form.cleaned_data['adhar_Number']
            if Detail.objects.filter(adhar_Number=adhar_number).exists():
                print("yes THE DATA IS EXIT THER IN DATABASE")
                messages.error(request,"User already in database")
            else:
                form.save()
                messages.success(request,"Your Response is Subimited")
    else:
        form = DetailForms() 

    return render(request, 'index.html', {'forms': form})