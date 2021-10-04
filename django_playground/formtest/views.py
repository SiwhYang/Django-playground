from django import forms
from django.shortcuts import render
from formtest.formssss import User_Form,UserProfile_Info_form


#login module
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect , HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required



def index(request):
    return render(request,'formtest/index.html')

def Registration(request):
    registered = False
    if request.method == "POST":
        user_form = User_Form(data=request.POST)
        profile_form = UserProfile_Info_form(data=request.POST)
    
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            #if 'profile_pic' in request.FILES:
            #profile.Profile_Picture = request.FILES['Profile_Picture']
            #profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = User_Form()
        profile_form = UserProfile_Info_form()

        
    context = {
            'User_Form':User_Form,
            'UserProfile_Info_form':UserProfile_Info_form,
            'registered':registered 
        }
    return render (request, 'formtest/Registration.html',context)

@login_required
def user_log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('formtest:index'))

def user_log_in(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)

        if user is not None :     #if we have user
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('formtest:index'))
            else:
                return HttpResponse('uesr not active')
        else:
            print("login fail")
            print("username : {} and password : {} ".format(username,password) )
            return HttpResponse("login fail !!!")
    else:
        return render(request,'formtest/login.html')


def test(request):
    N = 20
    context = {
        "data" : 99,
    }
    return render (request, 'formtest/test.html',context)
