from django import forms
from django.shortcuts import render
from . import formssss
# Create your views here.


def index(request):
    return render(request,'formtest/index.html')

def formpage(request):
    form = formssss.FormName
    
    return render(request,'formtest/form_page.html',{'form':form})