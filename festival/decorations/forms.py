
from django import forms
from .models import *
import os
from django.core.exceptions import ValidationError

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
            result = single_file_clean(data, initial)
        return result
class decorationsform(forms.ModelForm):
    dec_image = MultipleFileField(validators=[validate_image])
    dec_video = MultipleFileField(validators=[validate_video])

    class Meta:
        model = decorations
        fields = ['dec_title','dec_desc','dec_image','dec_video','amount']
        widgets = {
            "dec_title" : forms.TextInput(attrs={'class':'form-control','style':'height :50px;'}),
            "dec_desc" : forms.Textarea(attrs={'class':'form-control','style':'height :50px;'}),
            "dec_image" : forms.FileInput(attrs={'class':'form-control','style':'height :50px;'}),
            "dec_video" : forms.FileInput(attrs={'class':'form-control','style':'height :50px;'}),
            "amount" : forms.NumberInput(attrs={'class':'form-control','style':'height :50px;'}),
        }
        help_texts = {
            'dec_title' : None
        }
        labels ={
            'dec_title':'Decoration title',
            'dec_desc':'Decoration description',
            'dec_image':'Decoration images',
            'dec_video':'Decoration videos',
            'amount':'Amount Per Hour',
        }    
        




class EditdecForm(forms.ModelForm):
    
    class Meta:
        model = Register
        fields = ['username','email','contact','experience','street','pin','city','idproof','profile','address']
        widgets = {
            "username" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "email" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "contact" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "experience" : forms.Textarea(attrs={'class':'form-input','style':'width : 90%;height:150px'}),
            "address" : forms.Textarea(attrs={'class':'form-input','style':'width : 90%;height:150px'}),
            "pin" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "city" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "street" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "idproof" : forms.FileInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "profile" : forms.FileInput(attrs={'class':'form-input','style':'width : 90%;'}),

        }
        help_texts = {
            'username' : None
        }
       