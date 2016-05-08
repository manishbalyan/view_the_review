"""Import related to faculty forms."""
from django import forms
from django.contrib.auth.models import User
from faculty.models import UserProfileF


class UserForm(forms.ModelForm):
    """User for faculty."""

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        """It define UserForm."""

        model = User
        fields = ('username', 'email', 'password')

    # clean email field
    def clean_email(self):
        """Method to clean user email."""
        email = self.cleaned_data["email"]
        try:
            User._default_manager.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('duplicate email')

# modify save() method so that we can set user.is_active to False when we first create our user
    def save(self, commit=True):
        """Save method for UserForm."""
        user = super(UserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.is_active = False  # not active until he opens activation link
            user.save()
        return user


class UserProfileFormF(forms.ModelForm):
    """User for faculty."""

    CHOICES = (('CSE', 'CSE'), ('IT', 'IT'), ('ECE', 'ECE'), ('ME', 'ME'), ('CE', 'CE'), ('EN', 'EN'), ('WARDEN', 'WARDEN'))
    department = forms.ChoiceField(choices=CHOICES)
    i_agree = forms.BooleanField(required=True, label='I accept the Privacy Statement that all my data is visible to admin and i will be guilty if i found of any misbehave.')

    class Meta:
        """It describe UserProfileF form."""

        model = UserProfileF
        fields = ('faculty_id', 'department', 'profile_pic', 'i_agree')
