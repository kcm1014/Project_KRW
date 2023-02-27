from django.shortcuts import render

def index(reqeust):
    return render(reqeust,'main/index.html')
