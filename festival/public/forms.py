
from django import forms
from .models import *
GENDER_CHOICES = [
        ('', '--------------------Select gender----------------------------------------------------------'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ]
class LoginForm(forms.ModelForm):
    
    class Meta:
        model = Register
        fields = ['username','password']
        widgets = {
            "username" : forms.TextInput(attrs={'class':'form-control','style':''}),
            "password" : forms.PasswordInput(attrs={'class':'form-control','style':''})
        }
        help_texts = {
            'username' : None
        }
        
class RegaForm(forms.ModelForm):
    
    class Meta:
        model = Register
        fields = ['username','password','email','contact','profile']
        widgets = {
            "username" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "email" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "contact" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "password" : forms.PasswordInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "profile" : forms.FileInput(attrs={'class':'form-input','style':'width : 90%;'}),
        }
        help_texts = {
            'username' : None,
            'email' : '',
            'contact' : '',
            'experience' : '',
            'address' : '',
            'password' : '',



        }      
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = False  
class RegbForm(forms.ModelForm):
    
    class Meta:
        model = Register
        fields = ['username','password','email','contact','experience','street','pin','city','idproof','profile','address']
        widgets = {
            "username" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "email" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "contact" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "experience" : forms.NumberInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'in Years....'}),
            "address" : forms.Textarea(attrs={'class':'form-input','style':'width : 90%;height:150px'}),
            "password" : forms.PasswordInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "pin" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "city" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "street" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "idproof" : forms.FileInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "profile" : forms.FileInput(attrs={'class':'form-input','style':'width : 90%;'}),




        }
        help_texts = {
            'username' : None
        }  
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = False  
class RegcForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-input', 'style': 'width: 90%;'}))

    class Meta: 
        model = Register
        fields = ['username','password','email','contact','experience','dob','street','city','pin','idproof','profile','pr_type','address']
        widgets = {
            "username" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'Username'}),
            "email" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "contact" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "profile" : forms.FileInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "address" : forms.Textarea(attrs={'class':'form-input','style':'width : 90%;height:150px'}),
            "street" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "city" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "pin" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "idproof" : forms.FileInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "experience" : forms.NumberInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'in Years....'}),
            "password" : forms.PasswordInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "dob":forms.DateInput(attrs={'class':'form-input','style':'width : 90%;','type':'date'}),
           
            "pr_type" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;'}),
        }
        help_texts = {
            'username' : None,
            
        } 
        labels ={
            'pr_type':'Program Type',
           
        }    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = False                  


class RegdForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-input', 'style': 'width: 90%;'}))
    class Meta:
        model = Register
        fields = ['username','password','email','contact','gender','idproof','profile']
        widgets = {
            "username" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "email" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "contact" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "password" : forms.PasswordInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "idproof" : forms.FileInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "profile" : forms.FileInput(attrs={'class':'form-input','style':'width : 90%;'}),
        }
        help_texts = {
            'username' : None
        }   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = False                               