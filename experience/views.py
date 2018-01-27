from django.shortcuts import render
from .models import Activity
# Create your views here.
def experience_list(request):
    activities = Activity.objects.all()
    return render(request, 'experience/experience_list.html', {'activities':activities})
