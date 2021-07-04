from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from .forms import DigitalFilesForm
from .models import DigitalFiles
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request,'digitalfile/home.html')
def userpage(request):
    return render(request,'digitalfile/userpage.html')
def signupuser(request):
    if request.method=='GET':
        return render(request,'digitalfile/signupuser.html',{'form':UserCreationForm()})
    else:
        #Create a new User
        if request.POST['password1']==request.POST['password2']:
            try:
                user= User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                group=Group.objects.get(name='costumers')
                user.groups.add(group)
                return redirect ('loginuser')
            except IntegrityError:
                return render(request,'digitalfile/signupuser.html',{'form':UserCreationForm(),'error':'Username has already been taken.'})
        else:
            #tell the user the passwords didn't match
            return render(request,'digitalfile/signupuser.html',{'form':UserCreationForm(),'error':'Passwords did not match.'})
@unauthenticated_user
def loginuser(request):
    if request.method=='GET':
        return render(request,'digitalfile/loginuser.html',{'form':AuthenticationForm()})
    else:
        user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'digitalfile/loginuser.html',{'form':AuthenticationForm(), 'error':'Username and password did not match.'})
        else:
            login(request,user)
            return redirect ('home')
@login_required
def logoutuser(request):
    if request.method=='POST':
        logout(request)
        return redirect('homeUser')
@login_required
def digitalfiles(request):
    digitalfiles=DigitalFiles.objects.all()
    return render(request, 'digitalfile/digitalfiles.html',{'digitalfiles':digitalfiles})

@login_required
@allowed_users(allowed_roles=['admin',])
def createfiles(request):
    #similar to signin up
    if request.method == 'POST':
        form = DigitalFilesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('digitalfiles')
    else:
        form = DigitalFilesForm()
    return render(request, 'digitalfile/createfile.html', {
        'form': form
    })

@login_required
@allowed_users(allowed_roles=['admin',])
def updatefiles(request, file_pk):
    digitalfile=get_object_or_404(DigitalFiles, pk=file_pk)
    if request.method=='GET':
        form=DigitalFilesForm(instance=digitalfile)
        return render(request,'digitalfile/updatefiles.html',{'digitalfile':digitalfile,'form':form})
    else:
        try:
            form=DigitalFilesForm(request.POST,request.FILES,instance=digitalfile)
            form.save()
            return redirect('digitalfiles')
        except ValueError:
            return render(request,'digitalfile/updatefiles.html',{'digitalfile':digitalfile,'form':form,'error':'Bad info'})

@login_required
@allowed_users(allowed_roles=['admin',])
def deletefiles(request,file_pk):
    digitalfile=get_object_or_404(DigitalFiles, pk=file_pk)
    if request.method=='POST':
        digitalfile.delete()
        return redirect('digitalfiles')
def homeUser(request):
    return render(request,'digitalfile/homeUser.html')
def CreateFilesUser(request):
    #similar to signin up
    if request.method == 'POST':
        form = DigitalFilesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homeUser')
    else:
        form = DigitalFilesForm()
    return render(request, 'digitalfile/createFileUser.html', {
        'form': form
    })
