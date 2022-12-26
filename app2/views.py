from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def jyothi(request):
    return HttpResponse('i am lucky to have u as a friend')
def uma(request):
    return HttpResponse('<marquee>i am lucky to have roommates like u</marquee>')    
