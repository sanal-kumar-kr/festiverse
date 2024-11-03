from django.shortcuts import render
from public.models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.core.exceptions import PermissionDenied
from .forms import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
# @login_required(login_url='/login')
# def usersreq(request,ut):
#     if request.user.usertype==1:
#         print("______________________dfsgd------------------------------------------")
#         if ut==2:
#             data = Register.objects.filter(status=0,usertype=2)
#         elif ut==3:
#             data = Register.objects.filter(status=0,usertype=3)
#         elif ut==4:      
#             data = Register.objects.filter(status=0,usertype=4)  
#         elif ut==0:
#             data = Register.objects.filter(status=0,usertype=4)  
#         return render(request,'user_request.html',{'users_req_data':data})
#     else:
#         raise PermissionDenied 
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
    
    
@login_required(login_url='/login')    
def decision(request,uid,dec):
    if request.user.usertype==1:
        user=Register.objects.get(id=uid)
        if dec==1:
            user.status=1
            user.save()
        elif dec==2:
            user.status=2
            user.save()
        return redirect('/')    
    else:
        raise PermissionDenied 
    


    
@login_required(login_url='/login')    
def decision(request,uid,dec):
    if request.user.usertype==1:
        user=Register.objects.get(id=uid)
        if dec==1:
            user.status=1
            user.save()
        elif dec==2:
            user.status=2
            user.save()
        return redirect('/')    
    else:
        raise PermissionDenied 

@login_required(login_url='/login')
def users(request,ut):
    if request.user.usertype==1:
        print("______________________dfsgd------------------------------------------")
        if ut==2:
            data = Register.objects.filter(status=1,usertype=2)
        elif ut==3:
            data = Register.objects.filter(status=1,usertype=3)
        elif ut==4:      
            data = Register.objects.filter(status=1,usertype=4)  
        elif ut==0:
            data = Register.objects.filter(status=1,usertype=0)  
        return render(request,'users.html',{'users_data':data})
    else:
        raise PermissionDenied 
    
    
@login_required(login_url='/login')
def edituser(request,uid):
    if request.user.usertype==1 or request.user.id==uid:
        data=Register.objects.get(id=uid)
        if request.method == 'POST':
            form = EdituserForm(request.POST,instance=data)
            print(data)
            print(form.is_valid())
          
            if form.is_valid():
                form.save()
                return redirect('/')
          
        else:   
            form = EdituserForm(instance=data)
        return render(request,'edituser.html',{'form':form,'ut':data.usertype})
    else:
        raise PermissionDenied     
    

@login_required(login_url='/login')
def editdec(request,uid):
    if request.user.usertype==1 or request.user.id==uid:
        data=Register.objects.get(id=uid)
        if request.method == 'POST':
            form = EditdecForm(request.POST,instance=data)
            print(data)
            print(form.is_valid())
          
            if form.is_valid():
                form.save()
                return redirect('/')
          
        else:   
            form = EditdecForm(instance=data)
        return render(request,'editdec.html',{'form':form,'ut':data.usertype})
    else:
        raise PermissionDenied         
    
@login_required(login_url='/login')
def editart(request,uid):
    if request.user.usertype==1 or request.user.id==uid:
        data=Register.objects.get(id=uid)
        if request.method == 'POST':
            form = EditartistForm(request.POST,instance=data)
            print(data)
            print(form.is_valid())
          
            if form.is_valid():
                form.save()
                return redirect('/')
          
        else:   
            form = EditartistForm(instance=data)
        return render(request,'editart.html',{'form':form,'ut':data.usertype})
    else:
        raise PermissionDenied     
@login_required(login_url='/login')
def deleteuser(request,uid):
    if request.user.usertype==1:
        
        data=Register.objects.get(id=uid)
        data.delete()
        return redirect('/')
    else:
        raise PermissionDenied         
    


