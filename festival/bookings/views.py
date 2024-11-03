from django.shortcuts import render
from .models import *
from django.shortcuts import render,redirect
from django.core.exceptions import PermissionDenied
from .forms import *
from public.models import *
from decorations.models import *
from django.contrib import messages
from django.core.mail import send_mail,EmailMessage
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
    

def view_dpro(request,uid):
      data=programs.objects.filter(art_id=uid)
      return render(request, 'programs.html',{'data':data,'uid':uid})
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

def view_bookings(request,id):
      if request.user.usertype ==3:
        data=bookings.objects.filter(decid=id)
        return render(request, 'view_dec_booking.html',{'data':data})
      elif request.user.usertype == 4: 
        data=bookings.objects.filter(pgid=id)
        return render(request, 'view_program_bookings.html',{'data':data})
      elif request.user.usertype == 0:
        print("qhfguersegurhbgeurgbhruhgerhgerkewetrter",request.user.usertype)

        data=bookings.objects.filter(uid=id)
        return render(request, 'view_user_booking.html',{'data':data})
      elif request.user.usertype == 1:
        us=Register.objects.get(id=id)
        if us.usertype == 3:
            data=bookings.objects.filter(decid__dec_id=id)
            return render(request, 'view_dec_booking.html',{'data':data})
        elif us.usertype == 4:  
            data=bookings.objects.filter(pgid__art_id=id)
            return render(request, 'view_program_bookings.html',{'data':data})  
   
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
def bookuser(request,fuid):
    form=addbookingform(request.POST,request.FILES)
    # last_inserted_id=''
    if request.method=="POST" and fuid!=0:
        form.is_valid()
        uid=request.user.id
        date=form.cleaned_data['date']
        program=decorations.objects.get(id=fuid)

        uni=bookings.objects.filter(date=date,decid=fuid).first()
        if uni:
            messages.success(request, f'Already Booked !', extra_tags='user_reg')
            return redirect('/')


        if form.is_valid():
            new_booking= bookings.objects.create(
                decid=decorations.objects.get(id=fuid),
                uid=Register.objects.get(id=uid),
                date=form.cleaned_data['date'],
                stime=form.cleaned_data['stime'],
                district=form.cleaned_data['district'],
                location=form.cleaned_data['location'],
                etime=form.cleaned_data['etime']

            )
            # last_inserted_id = new_booking.id
            return render(request,"form.html",{'form':form,'purpose':'payment','amount':program.amount})
    elif request.method=="POST" and fuid==0:
        
        print("________________enter enetr eeneter _________________________")
        # la_id=bookings.objects.all().pop(-1)
        la_id=bookings.objects.latest('id')
        la_bk=bookings.objects.get(id=la_id.id)
        la_bk.status=1
        la_bk.save()
        subject = 'Payment SuccessFul'
        message = 'You Have a Booking at '+str(la_bk.date)
        from_email =  'Festiverse <nidhinreigns@gmail.com>'
        if la_bk.decid:

            recipient_list = [la_bk.decid.dec_id.email]
        elif la_bk.pgid: 
            recipient_list = [la_bk.pgid.art_id.email]
   
        send_mail(subject, message, from_email, recipient_list)
        email = EmailMessage(subject, message,from_email=from_email,to=recipient_list)
        email.send()
        messages.success(request, f'Booking Successfull !', extra_tags='user_reg')
        return redirect('/')
        

 
    else:
        form=addbookingform()
        return render(request,"form.html",{'form':form,'purpose':'book'})


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
def add_programs(request,id):
    form=programsform(request.POST,request.FILES)
    if request.method=="POST":
        if form.is_valid():
            dec=form.save(commit=False)
            dec.art_id=Register.objects.get(id=id)
            dec.save()
            files = request.FILES.getlist('art_image')
            if files:
                for file in files:
                    file_obj=File.objects.create(files=file)
                    dec.art_image.add(file_obj)
            vidfiles = request.FILES.getlist('art_video')
            if vidfiles:
                for file in vidfiles:
                    file_obj=decFile.objects.create(files=file)
                    dec.art_video.add(file_obj)
            return redirect('/')
        else:
            print(form.errors)

    else:
        form=programsform()
    
    return render(request, 'add_dec.html',{'form':form,'title':'Add programs'})


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
def edit_program(request,id):
    data=programs.objects.get(id=id)
    form=programsform(request.POST,request.FILES,instance=data)
    if request.method=="POST":
        if form.is_valid():

            decoration_instance = form.save(commit=False)
            decoration_instance.save()
            if 'art_image' in request.FILES:
                decoration_instance.art_image.clear()  # Clear existing files if necessary
                for file in request.FILES.getlist('art_image'):
                    file_instance = File.objects.create(files=file)
                    decoration_instance.art_image.add(file_instance)

            # Handle video uploads
            if 'art_video' in request.FILES:
                decoration_instance.art_video.clear()  # Clear existing files if necessary
                for file in request.FILES.getlist('art_video'):
                    file_instance = decFile.objects.create(files=file)
                    decoration_instance.art_video.add(file_instance)

            decoration_instance.save()  # Save the m2m relationships
            return redirect('/')
        else:
            print(form.errors)

    else:
        form=programsform(instance=data)
    return render(request, 'add_dec.html',{'form':form})

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
def delete_program(request,id):
    data=programs.objects.get(id=id)
    data.delete()
    return redirect('/')
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
def cancelbook(request,id):
    data=bookings.objects.get(id=id)
    if data.decid:
        emaildet=data.decid.dec_id.email
    
    elif data.pgid:
        emaildet=data.pgid.art_id.email
   
    subject = 'Booking Cancelled'
    message = 'Your Booking on '+str(data.date)+' Cancelled By User'
    from_email =  'Festiverse <nidhinreigns@gmail.com>'
    recipient_list = [emaildet]
    send_mail(subject, message, from_email, recipient_list)
    email = EmailMessage(subject, message,from_email=from_email,to=recipient_list)
    email.send()
    data.delete()
    return redirect('/view_bookings/'+str(request.user.id))


    
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
def bookpro(request,fuid):
    form=addbookingform(request.POST,request.FILES)
    # last_inserted_id=''
    if request.method=="POST" and fuid!=0:
        form.is_valid()
        uid=request.user.id
        date=form.cleaned_data['date']
        program=programs.objects.get(id=fuid)
        uni=bookings.objects.filter(date=date,pgid=fuid).first()
        if uni:
            messages.success(request, f'Already Booked !', extra_tags='user_reg')
            return redirect('/')

        if form.is_valid():
            new_booking= bookings.objects.create(
                pgid=programs.objects.get(id=fuid),
                uid=Register.objects.get(id=uid),
                date=form.cleaned_data['date'],
                stime=form.cleaned_data['stime'],
                district=form.cleaned_data['district'],
                location=form.cleaned_data['location'],
                etime=form.cleaned_data['etime']

            )
            # last_inserted_id = new_booking.id
            return render(request,"form.html",{'form':form,'purpose':'payment','amount':program.amount})
    elif request.method=="POST" and fuid==0:
        
        print("________________enter enetr eeneter _________________________")
        # la_id=bookings.objects.all().pop(-1)
        la_id=bookings.objects.latest('id')
        la_bk=bookings.objects.get(id=la_id.id)
        la_bk.status=1
        la_bk.save()
        subject = 'Payment SuccessFull'
        message = 'Your Have a Booking at '+str(la_bk.date)
        from_email =  'Festiverse <nidhinreigns@gmail.com>'
        recipient_list = [la_bk.pgid.art_id.email]
        send_mail(subject, message, from_email, recipient_list)
        email = EmailMessage(subject, message,from_email=from_email,to=recipient_list)
        email.send()
        return redirect('/')
         
    else:
        form=addbookingform()
        return render(request,"form.html",{'form':form,'purpose':'book'})


def view_prg(request,id):
      data=programs.objects.filter(id=id)
      return render(request, 'view_prg.html',{'data':data})