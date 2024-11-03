from django import forms
from public.models import *
GENDER_CHOICES = [
        ('', '--------------------Select gender----------------------------------------------------------'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ]
class EditOrgForm(forms.ModelForm):
    
    class Meta:
        model = Register
        fields = ['username','email','contact','experience','address','amountperhour','specialskills']
        widgets = {
            "username" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "email" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "contact" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "experience" : forms.Textarea(attrs={'class':'form-input','style':'width : 90%;height:150px'}),
            "amountperhour" : forms.NumberInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "specialskills" : forms.Textarea(attrs={'class':'form-input','style':'width : 90%;height:150px'}),
            "address" : forms.Textarea(attrs={'class':'form-input','style':'width : 90%;height:150px'}),

        }
        help_texts = {
            'username' : None,
            'email' : '',
            'contact' : '',
            'experience' : '',
            'address' : '',
           



        }    



class EditartistForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-input', 'style': 'width: 90%;'}))

    class Meta: 
        model = Register
        fields = ['username','email','contact','experience','amountperhour','dob','specialskills','street','city','pin','idproof','profile','pr_type','address']
        widgets = {
            "username" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "email" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "contact" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "profile" : forms.FileInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "address" : forms.Textarea(attrs={'class':'form-input','style':'width : 90%;height:150px'}),
            "street" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "city" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "pin" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "idproof" : forms.FileInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "experience" : forms.Textarea(attrs={'class':'form-input','style':'width : 90%;height:150px'}),
            "specialskills" : forms.Textarea(attrs={'class':'form-input','style':'width : 90%;height:150px'}),
            "dob":forms.DateInput(attrs={'class':'form-input','style':'width : 90%;','type':'date'}),
            "amountperhour" : forms.NumberInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "pr_type" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;'}),
        }
        help_texts = {
            'username' : None,
            
        }  



class EdituserForm(forms.ModelForm):
   
    
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-input', 'style': 'width: 90%;'}))
    class Meta:
        model = Register
        fields = ['username','email','contact','gender','profile']
        widgets = {
            "username" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "email" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "contact" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "profile" : forms.FileInput(attrs={'class':'form-input','style':'width : 90%;'}),
        }
        help_texts = {
            'username' : None
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
                 