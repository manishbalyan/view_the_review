"""imports used."""
from django import forms
from django.contrib.auth.models import User
from vtr.models import UserProfile, Query


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    CHOICES = (('CSE', 'CSE'), ('IT', 'IT'), ('ECE', 'ECE'), ('ME', 'ME'), ('CE', 'CE'), ('EE', 'EE'))
    CHOICES1 = ((1, '1'), (2, '2'), (3, '3'), (4, '4'))
    branch = forms.ChoiceField(choices=CHOICES)
    year = forms.ChoiceField(choices=CHOICES1, widget=forms.RadioSelect)
    class Meta:
        model = UserProfile
        fields = ('rollnumber', 'year', 'branch')


class QueryForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ['title', 'content', 'tag', ]