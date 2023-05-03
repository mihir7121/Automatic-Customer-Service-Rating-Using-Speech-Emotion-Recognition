from django.http import HttpResponse
from django.http.response import StreamingHttpResponse
from django.shortcuts import render, redirect
from .forms import AudioForm

import numpy as np

# Create your views here.
def index(request):
    return render(request, "app/index.html")

def upload_audio(request):
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return HttpResponse('successfully uploaded')
    else:
        form = AudioForm()
    return render(request, 'app/upload_audio.html', {'form': form})
