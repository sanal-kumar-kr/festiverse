
from django import forms
from .models import *
class messageform(forms.ModelForm):
    
    class Meta:
        model = inbox
        fields = ['message']
        widgets = {
            "message" : forms.Textarea(attrs={'class':'form-control','style':'height :50px;'}),
        }
        help_texts = {
            'message' : None
        }