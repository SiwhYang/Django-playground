from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'formtest/index.html')

def formpage(request):
    return render(request,'formtest/form_page.html')