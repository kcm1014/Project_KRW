from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def write(request):
    return render(request,'rate/write.html')
