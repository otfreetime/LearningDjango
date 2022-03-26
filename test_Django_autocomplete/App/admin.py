from django.contrib import admin

from .forms import *

from .models import *
# Register your models here.


admin.site.register(FakeAddress)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    form = PlaceForm