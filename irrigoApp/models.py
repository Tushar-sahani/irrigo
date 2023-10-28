from django.db import models

# Create your models here.

class Detail(models.Model):
    first_Name = models.CharField(max_length=20)
    last_Name = models.CharField(max_length=20)
    phone_Number = models.CharField(max_length=10)
    adhar_Number = models.CharField(max_length=12,primary_key=True)
    rfid = models.CharField(max_length=10)

    def __str__(self):
        return self.first_Name+" "+self.last_Name