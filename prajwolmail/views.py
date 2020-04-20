from django.shortcuts import render
from subscribe.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
# importing model
from .models import Email

def subscribe(request):
    subscribeForm = forms.Subscribe(request.POST or None)
    # if request.method == 'POST':
    if subscribeForm.is_valid():
        subscribeForm.save()
        subscribeForm = forms.Subscribe(request.POST)
        subject = 'Welcome to Corona Virus update'
        message = 'Hope you are staying safe'
        recepient = str(subscribeForm['email'].value())
        send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'prajwolmail/success.html', {'recepient': recepient})
    return render(request, 'prajwolmail/index.html', {'form':subscribeForm})



def mass_email(request):
    subject = "test mass subject"
    message = "test mass message"
    from_email = EMAIL_HOST_USER
    # receipent list
    emailList =[]
    for email in Email.objects.all():
        emailList.append(email.email)
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, emailList)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')
    # print(emailList)
    # return HttpResponse('mass email sending')