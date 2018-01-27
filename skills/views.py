from django.shortcuts import render
from .models import Skill

# Create your views here.
def skills_list(request):
    skills = Skill.objects.all()
    return render(request, 'skills/skills_list.html', {'skills':skills})
