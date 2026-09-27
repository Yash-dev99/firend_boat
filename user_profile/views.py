from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.


def user_page(request,user_name):
    if UserDim.objects.filter(user_name=user_name).exists():
        return HttpResponse("Hi u/%s, let's kill the reddit" %user_name)
    else:
        return HttpResponse("no user found")