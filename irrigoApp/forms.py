
from django import forms
from .models import Detail

class DetailForms(forms.ModelForm):
    class Meta:
        model = Detail
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_Name'].widget.attrs['class'] = 'form-control'
        self.fields['last_Name'].widget.attrs['class'] = 'form-control'
        self.fields['phone_Number'].widget.attrs['class'] = 'form-control'
        self.fields['adhar_Number'].widget.attrs['class'] = 'form-control'
        self.fields['rfid'].widget.attrs['class'] = 'form-control'


    def clean(self):
        cleaned_data = super().clean()
        adhar_number = cleaned_data.get('adhar_Number')
        phone_number = cleaned_data.get('phone_Number')
        
        if adhar_number and len(adhar_number) != 12:
            self.add_error('adhar_Number',"Adhar Number Must be 12 Digits")
        
        if phone_number and len(phone_number) != 10:
            self.add_error('phone_Number',"Phone Number Must be 10 Digits")

