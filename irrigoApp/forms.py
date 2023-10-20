from django import forms
from .models import Detail
class DetailForms(forms.ModelForm):
    class Meta:
        model = Detail
        fields = "__all__"