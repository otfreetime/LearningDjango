# forms.py
from django import forms
# from crispy_forms.layout import Submit
# from crispy_forms.helper import FormHelper
from django.views.generic import CreateView
from .models import  PostModel


class PostForm(forms.ModelForm):

    class Meta:
        model = PostModel
        fields = "__all__"


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


# class generateForm(forms.ModelForm):

#     class Meta:
#         model = GenerateModel
#         fields = "__all__"
#         widget=forms.DateTimeInput(attrs={
#             'class': 'form-control datetimepicker-input',
#             'data-target': '#datetimepicker1'
#         })



#class createCode(forms.Form):
#    code  = forms.CharField(label="Name", max_length=200)
#    endesc = forms.CharField(label="Name", max_length=200)
#    remarks = forms.CharField(label="Name", max_length=200)
#    ardesc =  forms.CharField(label="Name", max_length=200)

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
