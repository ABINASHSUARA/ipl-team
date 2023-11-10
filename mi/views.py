from django.shortcuts import render
from django.http import HttpResponse

def rohit(request):
    return render(request,'rohit.html')

def bumrah(request):
    return HttpResponse("boom boom")
# Create your views here.
