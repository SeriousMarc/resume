from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.contact, name='contact_home'),
    path('success/', views.success, name='contact_success'),
]
