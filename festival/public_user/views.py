from django.shortcuts import render
from public.models import *
from django.contrib import messages
from.models import*
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.core.exceptions import PermissionDenied
from .forms import *

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
def Search_user(request, ut):
    if request.user.usertype == 0 or request.user.usertype == 2:
        if ut == 4:
            data = Register.objects.filter(status=1,usertype=4)
        elif ut == 3:
            data = Register.objects.filter(status=1,usertype=3)
        # else:
        #     # Handle other user types or return all users if needed
        #     data = Register.objects.all()

        # Handling search functionality
        search_query = request.POST.get('search')
        if search_query:
            data = data.filter(username__icontains=search_query)

        return render(request, 'search_users.html', {'search_data': data})    
    else:
        raise PermissionDenied
   
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
def add_feedback(request,uid):
    if request.method=="POST":
        feedback.objects.create(
            fuserid=Register.objects.get(id=uid),
            uid=Register.objects.get(id=request.user.id),
            feedbackmsg=request.POST['comment'],
            ratings=request.POST['rating']
        )
        return redirect('/')
    else:
        return render(request,"add_feedback.html")

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
def view_feedbacks(request,uid):
    feedbacks=feedback.objects.filter(fuserid=uid)
    return render(request,"view_feedbacks.html",{'feedbacks':feedbacks,'user_id':uid})

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
def deletefeedback(request,fid):
    feedbacks=feedback.objects.filter(id=fid)
    feedbacks.delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))