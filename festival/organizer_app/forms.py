from django import forms
from .models import *

class Event(forms.ModelForm):
    decorators = forms.ModelChoiceField(queryset=Register.objects.filter(status=1, usertype=3), label='decorators', empty_label=None)
    artists = forms.ModelChoiceField(queryset=Register.objects.filter(status=1, usertype=4), label='artists', empty_label=None)
    
    class Meta:
        model = events
        fields = ['eventname', 'eventdescription', 'date', 'stime', 'etime', 'decorators', 'artists']
        widgets = {
            "eventname": forms.TextInput(attrs={'class': 'form-input', 'style': 'width: 90%;'}),
            "date": forms.DateInput(attrs={'class': 'form-input', 'style': 'width: 90%;', 'type': 'date'}),
            "eventdescription": forms.Textarea(attrs={'class': 'form-input', 'style': 'width: 90%;'}),
            "stime": forms.TimeInput(attrs={'class': 'form-input', 'style': 'width: 90%;', 'type': 'time'}),
            "etime": forms.TimeInput(attrs={'class': 'form-input', 'style': 'width: 90%;', 'type': 'time'}),
        }
        help_texts = {
            'eventname': None
        }
