from django import forms

from .models import Email

# class Subscribe(forms.Form):
#     Email = forms.EmailField()
#     def __str__(self):
#         return self.Email

class Subscribe(forms.ModelForm):

    class Meta:
        model = Email
        fields = ['email']