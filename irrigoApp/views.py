from django.shortcuts import render,redirect
from django.contrib import messages
from django.db import DatabaseError
from .models import Detail
from .forms import DetailForms
from .serializers import DetailSerializer
from rest_framework import status,generics
from rest_framework.views import APIView


from rest_framework.response import Response

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
                messages.error(request, "User with this Aadhar Number already exists.")
                render('index.html')
            else:
                form.save()
                messages.success(request,"Your Response is Subimited")
    else:
        form = DetailForms() 
    return render(request, 'index.html', {'forms': form})

class CheckRFIDExists(APIView):
    def get(self, request, rfid):
        try:
            # Check if the rfid exists in the database
            detail = Detail.objects.get(rfid=rfid)
            # If it exists, return a success response
            serializer = DetailSerializer(detail)
            return Response({
                'isFound':True,
                'message': 'Data found in the database',
                'details': serializer.data
            }, status=status.HTTP_200_OK)
        except Detail.DoesNotExist:
            # If it doesn't exist, return a not found response
            return Response({
                'isFound':False,
                'message': 'Data not found in the database'
            }, status=status.HTTP_404_NOT_FOUND)




