from django.shortcuts import render

# Create your views here.



def login(request):
    return render (request,'jseekers/login.html')

def home(request):
    return render (request,'jseekers/home.html')