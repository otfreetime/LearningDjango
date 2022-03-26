from dal import autocomplete
from django import forms
from .models import *

class AddressForm(forms.ModelForm):

    class Meta:
        model = FakeAddress
        fields = ('address',)




class PlaceForm(forms.ModelForm):
    address = forms.ModelChoiceField(
        queryset=FakeAddress.objects.all(),
        widget=autocomplete.ModelSelect2(url='address-autocomp')
    )

    class Meta:
        model = FakeAddress
        fields = ['address']