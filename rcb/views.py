from django.shortcuts import render
from django.http import HttpResponse

def virat(request):
    return render(request,'virat.html')

def abd(request):
    return HttpResponse("mr 360")

# Create your views here.
