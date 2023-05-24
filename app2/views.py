from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def app2_string(request):
    return HttpResponse('<h1><marquee>This is app2_string response</marque></marquee>')

def app2_html(request):
    return render(request,'app2_html.html')