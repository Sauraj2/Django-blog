#from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    #return HttpResponse('Hello world')
    return render(request,'Home.html')

def about(request):
    #return HttpResponse('About')
    return render(request,'About.html')
