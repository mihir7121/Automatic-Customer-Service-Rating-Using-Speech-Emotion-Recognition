from django.http import HttpResponse
from django.http.response import StreamingHttpResponse
from django.shortcuts import render, redirect
from .forms import AudioForm
from app.split_audio import ___

import numpy as np

# Create your views here.
def index(request):
    return render(request, "app/index.html")

def upload_audio(request):
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            response = redirect('/')
            return response
    else:
        form = AudioForm()
    return render(request, 'app/upload_audio.html', {'form': form})

def analysis(request):

    return render(request, 'app/analysis.html')