from django import forms
from django.contrib.auth.models import User
from faculty.models import UserProfileF


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    #clean email field
    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            User._default_manager.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('duplicate email')

#modify save() method so that we can set user.is_active to False when we first create our user
    def save(self, commit=True):        
        user = super(UserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.is_active = False  # not active until he opens activation link
            user.save()

        return user

class UserProfileFormF(forms.ModelForm):
    CHOICES = (('CSE', 'CSE'), ('IT', 'IT'), ('ECE', 'ECE'), ('ME', 'ME'), ('CE', 'CE'), ('EN', 'EN'),('WARDEN','WARDEN'))
    department = forms.ChoiceField(choices=CHOICES)
    profile_pic = forms.ImageField(required=False)

    class Meta:
        model = UserProfileF
        fields = ('faculty_id','department', 'profile_pic')
