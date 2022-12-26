from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def chinmayi(request):
    return HttpResponse('<i>friends are fake</i>')
def nanna(request):
    return HttpResponse('<marquee>i love my parents</marquee>')