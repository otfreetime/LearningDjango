# forms.py
import pandas as pd
from django import forms
#from django_select2 import forms as s2forms

#from .models import Code

class createForm(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField(required=False)


#class CodeWidget(s2forms.ModelSelect2Widget):
#    search_fields = [
#        "code__icontains",
#    ]


##class CodeForm(forms.Form):
##    code = forms.CharField(widget=s2forms.Select2Widget)

#class CodeForm(forms.ModelForm):
#    class Meta:
#        model = Code
#        fields = '__all__'
#        #widgets = {
#        #    'code': CodeWidget
#        #    }

#    def __init__(self, *args,**kwargs):
#        super().__init__(*args, **kwargs)
#        self.fields['code'].queryset= Code.objects.none()






#class AuthorWidget(s2forms.ModelSelect2Widget):
#    search_fields = [
#        "username__icontains",
#        "email__icontains",
#    ]


#class CoAuthorsWidget(s2forms.ModelSelect2MultipleWidget):
#    search_fields = [
#        "username__icontains",
#        "email__icontains",
#    ]


#class BookForm(forms.ModelForm):
#    class Meta:
#        model = models.Book
#        fields = "__all__"
#        widgets = {
#            "author": AuthorWidget,
#            "co_authors": CoAuthorsWidget,
#        }
