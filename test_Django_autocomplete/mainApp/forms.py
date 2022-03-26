from dal import autocomplete

from django import forms

from .modelsLanguage,  imports *

class PersonForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ('__all__')
        widgets = {
            'name': autocomplete.ModelSelect2(url='language-autocomplete')
        }
