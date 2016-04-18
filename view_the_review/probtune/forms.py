from django import forms
from probtune.models import QueryP
from taggit.forms import TagWidget

class QueryFormP(forms.ModelForm):
	show_user = forms.BooleanField(label='If You Want to Show Your Name With Query then Mark It', required=False)
	image = forms.ImageField(required=False)

	class Meta:
		model = QueryP
		fields = ['title','content','show_user','image','tags']
		widgets = {'tags': TagWidget()}