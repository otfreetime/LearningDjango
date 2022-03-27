from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# def detail(request):
#     dict_values = {'fav_color': ['blue','green']}
#     return render(request,'demo/example.html',dict_values)

def detail(request):
    '''
    Accepts a press release ID and returns the detail page
    '''
    #p = get_object_or_404(PressRelease, id=1)
    t = loader.get_template('demo/example.html')
    c = {'fav_color': ['blue','green']}
    rendered_template = t.render(c)
    return HttpResponse(rendered_template)