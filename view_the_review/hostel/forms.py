"""Import related to hostel forms."""
from django import forms
from hostel.models import QueryH
from taggit.forms import TagWidget


class QueryFormH(forms.ModelForm):
    """Query form for hostel queryies."""

    show_user = forms.BooleanField(label='If You Want to Show Your Name With Query then Mark It', required=False)
    image = forms.ImageField(required=False)

    class Meta:
        """It defines the QueryFormH."""

        model = QueryH
        fields = ['title', 'content', 'show_user', 'image', 'tags']
        widgets = {'tags': TagWidget()}
