from django import forms
from public.models import *
from .models import *
import os
from django.core.exceptions import ValidationError

class addbookingform(forms.ModelForm):
    
    class Meta:
        model = bookings
        fields = ['date', 'stime', 'etime','district','location']
        widgets = {
            "date": forms.DateInput(attrs={'class': 'form-input', 'style': 'width: 90%;','type':'date'}),
            "stime": forms.TimeInput(attrs={'class': 'form-input', 'style': 'width: 90%;','type':'time'}),
            "etime": forms.TimeInput(attrs={'class': 'form-input', 'style': 'width: 90%;','type':'time'}),
            "district": forms.Select(attrs={'class': 'form-input', 'style': 'width: 90%;'}),
            "location": forms.TextInput(attrs={'class': 'form-input', 'style': 'width: 90%;'}),
        }

        labels ={
            'stime':'Start time',
            'etime':'End time',
        }   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = False  

def validate_image(file):
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif','.avif']
    ext = os.path.splitext(file.name)[1]
    if ext.lower() not in valid_extensions:
        raise ValidationError('Unsupported file extension. Allowed extensions are: ' + ', '.join(valid_extensions))

def validate_video(file):
    valid_extensions = ['.mp4', '.avi', '.mov', '.wmv']
    ext = os.path.splitext(file.name)[1]
    if ext.lower() not in valid_extensions:
        raise ValidationError('Unsupported file extension. Allowed extensions are: ' + ', '.join(valid_extensions))




class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True
class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        kwargs.setdefault("required", False)  # Allow the field to be optional

        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = sin






class programsform(forms.ModelForm):
    art_image = MultipleFileField(validators=[validate_image])
    art_video = MultipleFileField(validators=[validate_video])
    class Meta:
        model = programs
        fields = ['art_title','art_desc','art_image','art_video','amount']
        widgets = {
            "art_title" : forms.TextInput(attrs={'class':'form-control','style':'height :50px;'}),
            "art_desc" : forms.Textarea(attrs={'class':'form-control','style':'height :50px;'}),
            "art_image" : forms.FileInput(attrs={'class':'form-control','style':'height :50px;'}),
            "amount" : forms.NumberInput(attrs={'class':'form-control','style':'height :50px,px;'}),
        }
        labels={
            'amount' : 'Amount Per Hour',
            'art_desc':'Art description',
           
        }     

