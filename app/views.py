from django.http import HttpResponse
from django.http.response import StreamingHttpResponse
from django.shortcuts import render
import numpy as np

# Create your views here.
def landing(request):
    return render(request, "app/landing.html")

def index(request):
    return render(request, "app/index.html")