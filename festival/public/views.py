from django.shortcuts import render
from django.contrib import messages

from .forms import *
from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
   
    return render(request, 'index.html')
def contact(request):
    return render(request, 'contact.html')
def service(request):
    return render(request, 'services.html')
def about(request):
    return render(request, 'about.html')
def la(request):
    return render(request, 'layout.html')
def Login(request):
    form = LoginForm()
    if request.method == "POST":
        user = authenticate(request,username=request.POST["username"],password=request.POST["password"] )
        if user is None :
            return render(request,'Login.html',{'form':form,'k':True})   
        elif user.status==1:
            print("helloooo")
            login(request, user)
            data = Register.objects.get(username=user)
            request.session['ut']=data.usertype
            data.usertype
            request.session['userid']=data.id
            request.session['is_loggedin']=True
            print()
            return redirect('/')
    else:
        form = LoginForm()
    return render(request,'Login.html',{'form':form}) 
@login_required(login_url='/login')
def Logout(request):
    auth.logout(request)
    return redirect('/')
def organizersreg(request):
    if request.method=='POST':
        form = RegaForm(request.POST,request.FILES)
        try:
            Register.objects.get(username=request.POST['email'])
            return render(request,'Register.html',{'form':form,'z':True})
        except Register.DoesNotExist:
            if form.is_valid():
                
                Register.objects.create_user(
                    username = form.cleaned_data["username"],
                    email = form.cleaned_data["email"],
                    password = form.cleaned_data["password"],
                    contact = form.cleaned_data["contact"],
                    address = form.cleaned_data["address"],
                    usertype = 2
                    )
                # subject = 'You are register Successfully By Admin'
                # message = 'Your Password Is' +str(password)
                # email_from = settings.EMAIL_HOST_USER
                # recipient_list = [email]
                
                # send_mail(subject,message,email_from,recipient_list)
                return redirect('/')
            else:
                messages.error(request, form.errors)

    else:
        form = RegaForm()
    return render(request,'Register.html',{'form':form,'user':'Organiser'})


def vendorsreg(request):
    if request.method=='POST':
        form = RegbForm(request.POST,request.FILES)
        try:
            Register.objects.get(username=request.POST['email'])
            return render(request,'Register.html',{'form':form,'z':True})
        except Register.DoesNotExist:
            print(request.POST)
            print(form.is_valid())
            if form.is_valid():
                print("valid")
                
                Register.objects.create_user(
                    username = form.cleaned_data["username"],
                    email = form.cleaned_data["email"],
                    password = form.cleaned_data["password"],
                    contact = form.cleaned_data["contact"],
                    address = form.cleaned_data["address"],
                    experience = form.cleaned_data["experience"],
                    profile=form.cleaned_data["profile"],
                    idproof=form.cleaned_data["idproof"],
                    pin = form.cleaned_data["pin"],
                    city=form.cleaned_data["city"],
                    street=form.cleaned_data["street"],
                    usertype = 3
                    )
                # subject = 'You are register Successfully By Admin'
                # message = 'Your Password Is' +str(password)
                # email_from = settings.EMAIL_HOST_USER
                # recipient_list = [email]
                
                # send_mail(subject,message,email_from,recipient_list)
                return redirect('/')
    else:
        form = RegbForm()
    return render(request,'decoratorreg.html',{'form':form,'user':'Decorator'})


def artistsreg(request):
    
    
    if request.method=='POST':
        form = RegcForm(request.POST,request.FILES)
        try:
            Register.objects.get(username=request.POST['email'])
            return render(request,'Register.html',{'form':form,'z':True})
        except Register.DoesNotExist:
            print(form.errors)
            if form.is_valid():
                
                Register.objects.create_user(
                    username = form.cleaned_data["username"],
                    email = form.cleaned_data["email"],
                    password = form.cleaned_data["password"],
                    contact = form.cleaned_data["contact"],
                    address = form.cleaned_data["address"],
                    experience = form.cleaned_data["experience"],
                    dob=form.cleaned_data['dob'],
                    profile=form.cleaned_data["profile"],
                    idproof=form.cleaned_data["idproof"],
                    gender=form.cleaned_data['gender'],
                    pin = form.cleaned_data["pin"],
                    city=form.cleaned_data["city"],
                    # pr_type=form.cleaned_data["pr_type"],
                    street=form.cleaned_data["street"],
                    # amountperhour = form.cleaned_data["amountperhour"],
                    # specialskills = form.cleaned_data["specialskills"],
                    usertype = 4
                    )
                # subject = 'You are register Successfully By Admin'
                # message = 'Your Password Is' +str(password)
                # email_from = settings.EMAIL_HOST_USER
                # recipient_list = [email]
                
                # send_mail(subject,message,email_from,recipient_list)
                return redirect('/')
    else:
        form = RegcForm()
    return render(request,'artistreg.html',{'form':form,'user':'Artist'})


def usersreg(request):
    
    if request.method=='POST':
        form = RegdForm(request.POST,request.FILES)
        try:
            Register.objects.get(username=request.POST['email'])
            return render(request,'Register.html',{'form':form,'z':True})
        except Register.DoesNotExist:
            print("valid123456")
            print(form.errors)

            if form.is_valid():
                print("valid")
                
                Register.objects.create_user(
                    username = form.cleaned_data["username"],
                    email = form.cleaned_data["email"],
                    password = form.cleaned_data["password"],
                    contact = form.cleaned_data["contact"],
                    profile = form.cleaned_data["profile"],
                    idproof=form.cleaned_data["idproof"],
                    gender=form.cleaned_data['gender'],
                    status=1,
                    usertype = 0
                    )
               
                return redirect('/')
            else:
                if 'email' in form.errors:
                        email_errors = form.errors['email']
                        for error in email_errors:
                            messages.error(request, error)    
    
    else:                        
        form = RegdForm()
    return render(request,'Register.html',{'form':form,'user':'Public'})



@login_required(login_url='/login')
def myprofile(request,uid):
    myprofile=Register.objects.get(id=uid)
    return render(request,"myprofile.html",{'myprofile':myprofile})
    