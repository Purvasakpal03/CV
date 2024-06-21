from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import math
from django.template import loader
from .models import pet


# Create your views here.
def demo(request):
    pi = math.pi
    return HttpResponse("<html> <body> <h1> <u> pi value %s" %pi)
    
def hello(request):
    return HttpResponse("hello world")

def dt(request):
    dt = datetime.now()
    msg = "unknown"
    if dt.hour < 12:
        msg = "Good Morning Today's date & time : %s" %dt
    elif dt.hour <= 16 & dt.hour > 12:
        msg = "Good Afternoon Today's date & time : %s" %dt
    else :
        msg = "Good Evening Today's date & time : %s" %dt
    
    return HttpResponse(msg)

def welcome(request):
    temp = loader.get_template('demohtmlpage.html')
    return HttpResponse(temp.render())

