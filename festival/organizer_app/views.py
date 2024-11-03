from django.shortcuts import render
from django.shortcuts import render

from .forms import *
from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/login')
def add_events(request):
        if request.method=="POST":
            if form.is_valid():
                
                Register.objects.create_user(
                    username = form.cleaned_data["username"],
                    email = form.cleaned_data["email"],
                    password = form.cleaned_data["password"],
                    contact = form.cleaned_data["contact"],
                    address = form.cleaned_data["address"],
                    perhouramount = form.cleaned_data["perhouramount"],

                    experience = form.cleaned_data["experience"],
                  
                    usertype = 4
                    )
                # subject = 'You are register Successfully By Admin'
                # message = 'Your Password Is' +str(password)
                # email_from = settings.EMAIL_HOST_USER
                # recipient_list = [email]
                
                # send_mail(subject,message,email_from,recipient_list)
                return redirect('/')
        else:
    
                form=Event()
                return render(request,"event_form.html",{'form':form})