from django import forms
from .models import members
from try_django.settings import DATE_INPUT_FORMATS
class staff_form(forms.ModelForm):
    DOB = forms.DateField(input_formats =  DATE_INPUT_FORMATS)
    class Meta:
        model = members
        fields = ['S_no', 'FirstName', 'LastName', 'DOB', 'Email', 'Address']

    

