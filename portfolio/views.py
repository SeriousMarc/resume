from django.shortcuts import render
from .models import Project
# Create your views here.
def portfolio_list(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/portfolio_list.html', {'projects':projects})
