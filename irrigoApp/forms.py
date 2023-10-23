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
   