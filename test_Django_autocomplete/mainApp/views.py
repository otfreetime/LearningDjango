from django.shortcuts import render
from .models import Language
from dal import autocomplete


# Create your views here.
def home(request):
    languages = Language.objects.all()
    return render(request,'mainApp/index.html',{"languages":languages})


class languageAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Language.objects.none()

        qs = Language.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs

