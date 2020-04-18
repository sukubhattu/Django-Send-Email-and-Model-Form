from django.shortcuts import render
from subscribe.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail
# Create your views here.

def subscribe(request):
    subscribeForm = forms.Subscribe(request.POST or None)
    # if request.method == 'POST':
    if subscribeForm.is_valid():
        subscribeForm.save()
        subscribeForm = forms.Subscribe(request.POST)
        subject = 'Welcome to Corona Virus update'
        message = 'Hope you are staying safe'
        recepient = str(subscribeForm['personEmail'].value())
        send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'prajwolmail/success.html', {'recepient': recepient})
    return render(request, 'prajwolmail/index.html', {'form':subscribeForm})