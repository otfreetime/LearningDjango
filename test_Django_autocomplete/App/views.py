from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
from faker import Faker
from .models import FakeAddress 
from .filters import AddressFilter
from dal import autocomplete
from tagging.models import Tag


#fake=Faker()
#for i in range(0, 100):
#    FakeAddress.objects.create(address=fake.address())

# Create your views here.

#def generate_data():

#    return JsonResponse({'status':200})

def home(request):
        return render(request,'App/index.html')


def search_address(request):
    address = request.GET.get('address')
    payload = []
    if address:
        fake_address_objs = FakeAddress.objects.filter(address__icontains=address)

        for fake_address_obj in fake_address_objs:
            payload.append(fake_address_obj.address)


    return JsonResponse({'status':200,'data':payload})

def search(request):
    address_list = FakeAddress.objects.all()
    address_filter = AddressFilter(request.GET, queryset=address_list)
    return render(request, 'app/address_list.html', {'filter': address_filter})

def address_form(request):
    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AddressForm()  

    return render(request, 'app/address_new.html', {'form': form})



class AddressAutocomp(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = FakeAddress.objects.all()
        if self.q:
            qs = qs.filter(address__istartswith=self.q)
        return qs