from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    print "hi"
    return render(request, "homepage.html", {})
