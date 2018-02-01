from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

def homepage(request):
    return render(request, 'homepage.html', {'MEDIA_URL':settings.MEDIA_URL})
