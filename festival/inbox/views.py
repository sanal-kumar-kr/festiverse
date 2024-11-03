from django.shortcuts import render
from .models import *
from itertools import chain

from .forms import *
from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.
def inbox_int(request):
    if request.user.usertype==3:
        data = Register.objects.filter(usertype__in=[0])
    elif request.user.usertype==4:    
        data = Register.objects.filter(usertype__in=[0])
    elif request.user.usertype==0:    
        data = Register.objects.filter(usertype__in=[3,4]) 
    return render(request, 'inbox.html',{'data':data})



def message(request,ptwoid):
     
    if request.method=='POST':
        form = messageform(request.POST,request.FILES)
       
        if form.is_valid():
            print("valid")
            
            inbox.objects.create(
                personone =Register.objects.get(id=request.user.id),
                persontwo = Register.objects.get(id=ptwoid),
                message = form.cleaned_data["message"],
                datetime=timezone.now()
               
                )
            # subject = 'You are register Successfully By Admin'
            # message = 'Your Password Is' +str(password)
            # email_from = settings.EMAIL_HOST_USER
            # recipient_list = [email]
            
            # send_mail(subject,message,email_from,recipient_list)
            data1=inbox.objects.filter(personone=request.user.id,persontwo=ptwoid)
            data2=inbox.objects.filter(personone=ptwoid,persontwo=request.user.id)
            merged_data = list(chain(data1, data2))
            merged_data.sort(key=lambda x: x.datetime) 



            return render(request,'message_interface.html',{'data':merged_data,'form':form})
    else:
        form = messageform()
        data1=inbox.objects.filter(personone=request.user.id,persontwo=ptwoid)
        data2=inbox.objects.filter(personone=ptwoid,persontwo=request.user.id)
        merged_data = list(chain(data1, data2))
        merged_data.sort(key=lambda x: x.datetime) 
        print(merged_data)
    return render(request,'message_interface.html',{'form':form,'data':merged_data})
   
