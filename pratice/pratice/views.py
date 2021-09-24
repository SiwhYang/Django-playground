from django.shortcuts import render
from . import form

def index(request):
    return render(request,'testuwiwps/index')

def FormNameTest(request):
    form = form.FormsName
    return render(request,'')
