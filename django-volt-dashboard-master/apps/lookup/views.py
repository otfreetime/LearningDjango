
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .forms import  PostForm
from .models import  PostModel

# Create your views here.

@login_required(login_url="/login/")
def index(request):
    return HttpResponse("Hello World")

@login_required(login_url="/login/")
def orderView(request):
    return HttpResponse("orderView")

# @login_required(login_url="/login/")
class PostView(CreateView):
    model=PostModel
    form_class=PostForm
    template_name = 'lookup/lookup.html'