from django import forms
from .models import Hood

class NewHoodForm(forms.ModelForm):
    class Meta:
        model = Hood
        exclude = ['user', 'pub_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
