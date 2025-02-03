from django.shortcuts import render
from django.http import HttpResponse

def firstfunc(request):
    return render(request,'hello.html')

