from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import render,redirect
from django.core.exceptions import PermissionDenied
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/login')
def usersreq(request, ut):
    if request.user.usertype == 1:
        if ut == 2:
            data = Register.objects.filter(status=0, usertype=2)
        elif ut == 3:
            data = Register.objects.filter(status=0, usertype=3)
        elif ut == 4:
            data = Register.objects.filter(status=0, usertype=4)


        

        return render(request, 'user_request.html', {'users_req_data': data})
    else:
        raise PermissionDenied
def add_complaint(request,art_dec):
    form=complaintform(request.POST,request.FILES)
    if request.method=="POST":
        if form.is_valid():
           complaint.objects.create(
            userid=Register.objects.get(id=request.user.id),
            dec_art_id=Register.objects.get(id=art_dec),
            title=form.cleaned_data['title'],
            complaint=form.cleaned_data['complaint'],
            datetime=timezone.now() 
               
           )
           return redirect('/')
    else:     
        form=complaintform()
        return render(request, 'add_complaint.html',{'form':form})

@login_required(login_url='/login')
def usersreq(request, ut):
    if request.user.usertype == 1:
        if ut == 2:
            data = Register.objects.filter(status=0, usertype=2)
        elif ut == 3:
            data = Register.objects.filter(status=0, usertype=3)
        elif ut == 4:
            data = Register.objects.filter(status=0, usertype=4)


        

        return render(request, 'user_request.html', {'users_req_data': data})
    else:
        raise PermissionDenied
def viewcomplaints(request,art_dec):
    if request.user.usertype == 0:
      data=complaint.objects.filter(dec_art_id=art_dec,userid=request.user.id)
      return render(request, 'view_complaints.html',{'data':data,'id':art_dec})
    elif request.user.usertype == 1:
      data=complaint.objects.filter(dec_art_id=art_dec)
      return render(request, 'view_complaints.html',{'data':data,'id':art_dec})
@login_required(login_url='/login')
def usersreq(request, ut):
    if request.user.usertype == 1:
        if ut == 2:
            data = Register.objects.filter(status=0, usertype=2)
        elif ut == 3:
            data = Register.objects.filter(status=0, usertype=3)
        elif ut == 4:
            data = Register.objects.filter(status=0, usertype=4)


        

        return render(request, 'user_request.html', {'users_req_data': data})
    else:
        raise PermissionDenied
def reply(request,id):
    form=responseform(request.POST,request.FILES)
    if request.method=="POST":
        if form.is_valid():
            data=complaint.objects.get(id=id)
            data.response = form.cleaned_data['response']
            data.save()
            return redirect('/')
    else:     
        form=responseform()
        return render(request,'respone.html',{'form':form})