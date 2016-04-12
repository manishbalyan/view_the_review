from django import forms
from django.contrib.auth.models import User
from vtr.models import UserProfileS, QueryS
from taggit.forms import TagWidget

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


class UserProfileFormS(forms.ModelForm):
    CHOICES = (('CSE', 'CSE'), ('IT', 'IT'), ('ECE', 'ECE'), ('ME', 'ME'), ('CE', 'CE'), ('EN', 'EN'))
    CHOICES1 = ((1, '1'), (2, '2'), (3, '3'), (4, '4'))
    branch = forms.ChoiceField(choices=CHOICES)
    year = forms.ChoiceField(choices=CHOICES1, widget=forms.RadioSelect)
    hostler = forms.BooleanField(required=False)
    profile_pic = forms.ImageField(required=False)
   
    class Meta:
        model = UserProfileS
        fields = ('rollnumber', 'year', 'branch', 'hostler', 'profile_pic')




class QueryFormS(forms.ModelForm):
    show_user = forms.BooleanField(label='If You Want to Show Your Name With Query then Mark It', required=False)
    
    class Meta:
        model = QueryS
        fields = ['title', 'content', 'show_user','tags']
        widgets = {'tags': TagWidget()}


class SearchForm(forms.Form):
    query = forms.CharField(label='Enter a keyword to search for',widget=forms.TextInput(attrs={'size': 32}))