"""imports related to forms."""
from django import forms
from django.contrib.auth.models import User
from vtr.models import UserProfileS, QueryS
from taggit.forms import TagWidget


class UserForm(forms.ModelForm):
    """User form for vtr."""

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        """This metaclass defines how a class userform behaves."""

        model = User
        fields = ('username', 'email', 'password')

    def clean_email(self):
        """Function to clean user email."""
        email = self.cleaned_data["email"]
        try:
            User._default_manager.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('duplicate email')

# modify save() method so that we can set user.is_active to False when we first create our user.
    def save(self, commit=True):
        """Save method for user form."""
        user = super(UserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.is_active = False  # not active until he opens activation link.
            user.save()

        return user


class UserProfileFormS(forms.ModelForm):
    """User prifile form extends user form."""

    CHOICES = (('CSE', 'CSE'), ('IT', 'IT'), ('ECE', 'ECE'), ('ME', 'ME'), ('CE', 'CE'), ('EN', 'EN'))
    CHOICES1 = ((1, '1'), (2, '2'), (3, '3'), (4, '4'))
    branch = forms.ChoiceField(choices=CHOICES)
    year = forms.ChoiceField(choices=CHOICES1, widget=forms.RadioSelect)
    hostler = forms.BooleanField(required=False)
    profile_pic = forms.ImageField(required=False)

    class Meta:
        """this class define how user profile form behaves."""

        model = UserProfileS
        fields = ('rollnumber', 'year', 'branch', 'hostler', 'profile_pic')


class QueryFormS(forms.ModelForm):
    """Form for students query."""

    show_user = forms.BooleanField(label='If You Want to Show Your Name With Query then Mark It', required=False)

    class Meta:
        """Define how student query form behaves."""

        model = QueryS
        fields = ['title', 'content', 'show_user', 'image', 'tags']
        widgets = {'tags': TagWidget()}
