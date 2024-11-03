from django.shortcuts import render
from .models import *
from itertools import chain
from .forms import *
from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
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
def view_dec(request,uid):
      print(uid)
      data=decorations.objects.filter(dec_id=uid)
      print(data)
      return render(request, 'view_dec.html',{'data':data,'uid':uid})

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

def add_dec(request,uid):
    form=decorationsform(request.POST,request.FILES)
    if request.method=="POST":
        if form.is_valid():
            dec=form.save(commit=False)
            dec.dec_id=Register.objects.get(id=uid)
            dec.save()
            files = request.FILES.getlist('dec_image')
            if files:
                for file in files:
                    file_obj=File.objects.create(files=file)
                    dec.dec_image.add(file_obj)
            vidfiles = request.FILES.getlist('dec_video')
            if vidfiles:
                for file in vidfiles:
                    file_obj=decFile.objects.create(files=file)
                    dec.dec_video.add(file_obj)
            # decorations.objects.create(
            #     dec_id=Register.objects.get(id=uid),
            #     dec_title=form.cleaned_data['dec_title'],
            #     dec_desc=form.cleaned_data['dec_desc'],
            #     dec_image=form.cleaned_data['dec_image'],
            #     amount=form.cleaned_data['dec_image']
            # )
            return redirect('/')
        else:
            print(form.errors)

    else:
        form=decorationsform()
    
    return render(request, 'add_dec.html',{'form':form,'uid':uid,'title':'Add Decorations'})


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


def editdecoration(request, id):
    data = decorations.objects.get(id=id)
    if request.method == "POST":
        form = decorationsform(request.POST, request.FILES, instance=data)
        if form.is_valid():
            decoration_instance = form.save(commit=False)
            decoration_instance.save()

            # Handle image uploads
            if 'dec_image' in request.FILES:
                decoration_instance.dec_image.clear()  # Clear existing files if necessary
                for file in request.FILES.getlist('dec_image'):
                    file_instance = File.objects.create(files=file)
                    decoration_instance.dec_image.add(file_instance)

            # Handle video uploads
            if 'dec_video' in request.FILES:
                decoration_instance.dec_video.clear()  # Clear existing files if necessary
                for file in request.FILES.getlist('dec_video'):
                    file_instance = decFile.objects.create(files=file)
                    decoration_instance.dec_video.add(file_instance)

            decoration_instance.save()  # Save the m2m relationships

            return redirect('/')
        else:
            print(form.errors)
    else:
        form = decorationsform(instance=data)

    return render(request, 'add_dec.html', {'form': form})

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


def deletedecoration(request,id):
    data=decorations.objects.get(id=id)
    data.delete()
    return redirect('/')

def decoration_detail(request,id):
      print(id)  
      data=decorations.objects.filter(id=id)
      print(data)
      return render(request, 'decorations.html',{'data':data})
