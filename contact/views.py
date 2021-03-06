from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            message += ' from: ' + from_email
            try:
                send_mail(subject, message, from_email, ['medivhbox@gmail.com'], fail_silently=True)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('contact:contact_success')
    return render(request, 'contact/contact.html', {'form':form})

def success(request):
    return render(request, 'contact/success.html')
