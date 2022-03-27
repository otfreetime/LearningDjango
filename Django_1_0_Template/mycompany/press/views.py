from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseServerError
from django.template import loader, Context
from press.models import PressRelease

# Create your views here.

def detail(request, pk):
    p = get_object_or_404(PressRelease, id=pk)

    t = loader.get_template('press/detail.html')
    c = {'press': p}
    rendered_template = t.render(c)
    return HttpResponse(rendered_template)

def press_list(request):
    '''
    Returns a list of press releases
    '''
    pl = get_list_or_404(PressRelease)
    t = loader.get_template('press/list.html')
    c = {'press_list': pl}
    return HttpResponse(t.render(c))

def functional_list_view(request):
	context ={ "dataset" : PressRelease.objects.all()}
	return render(request, "press/press_list_view.html", context)


def functional_detail_view(request, pk):
    
	context = { "press" :  PressRelease.objects.get(id=1)}
	return render(request, "press/press_detail_view.html", context)
