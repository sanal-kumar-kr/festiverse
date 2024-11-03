
from django import forms
from .models import *
class complaintform(forms.ModelForm):
    
    class Meta:
        model = complaint
        fields = ['complaint','title']
        widgets = {
            "title" : forms.TextInput(attrs={'class':'form-control','style':''}),
            "complaint" : forms.Textarea(attrs={'class':'form-control','style':'height :50px;'}),
        }
        help_texts = {
            'complaint' : None
        }


class responseform(forms.ModelForm):
    
    class Meta:
        model = complaint
        fields = ['response']
        widgets = {
            "complaint" : forms.Textarea(attrs={'class':'form-control','style':'height :50px;'}),
        }
       