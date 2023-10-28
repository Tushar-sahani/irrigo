from rest_framework import serializers
from .models import Detail

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Detail
        fields =['first_Name','last_Name','rfid']


