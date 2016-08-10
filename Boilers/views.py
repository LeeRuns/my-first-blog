from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def Boilerview(request):
    return HttpResponse("Hello, you have reached the Boilers page,to edit this go to the boilers view")
