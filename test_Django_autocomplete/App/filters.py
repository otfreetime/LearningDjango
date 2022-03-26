from .models import FakeAddress
import django_filters

class AddressFilter(django_filters.FilterSet):
    address = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = FakeAddress
        #fields = ['username', 'first_name', 'last_name', ]
        fields =['address']
