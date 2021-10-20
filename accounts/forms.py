from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class candidateform(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=False)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    resume = forms.FileField(required=False)

    class Meta:
        model = User
        fields = ("username", "email", "phone_number", "first_name", "last_name", "password1", "password2","resume")

    def save(self,commit=True):
        user = super(candidateform, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.phone_number = self.cleaned_data["phone_number"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user

class employerform(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "phone_number", "first_name", "last_name", "password1", "password2",)

    def save(self,commit=True):
        user = super(employerform, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.phone_number = self.cleaned_data["phone_number"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user