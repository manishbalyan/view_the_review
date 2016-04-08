from django import forms
from django.contrib.auth.models import User
from faculty.models import UserProfileF


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileFormF(forms.ModelForm):
    CHOICES = (('CSE', 'CSE'), ('IT', 'IT'), ('ECE', 'ECE'), ('ME', 'ME'), ('CE', 'CE'), ('EN', 'EN'),('WARDEN','WARDEN'))
    department = forms.ChoiceField(choices=CHOICES)
    profile_pic = forms.ImageField(required=False)

    class Meta:
        model = UserProfileF
        fields = ('faculty_id','department', 'profile_pic')
