from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def home_view(request:HttpRequest):
    # content = "hello world"
    
    return render(request,"main/base.html")