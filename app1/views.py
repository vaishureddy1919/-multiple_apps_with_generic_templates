from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def app1_string(request):
    return HttpResponse('<h1>This is app1_string response</h1>')

def app1_html(request):
    return render(request,'app1_html.html')