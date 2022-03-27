from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template, loader


def detail(request):
    dict_values = {'fav_color': 'blue'}
    template_string = loader.get_template('example.html').template
    c = Context(dict_values)
    t = Template(template_string)
    rendered_template = t.render(c)
    return HttpResponse(rendered_template)




# def detail(request):
#     dict_values = {'fav_color': 'blue'}
#     template_string = "My favorite color is {{ fav_color }}."
#     c = Context(dict_values)
#     t = Template(template_string)
#     rendered_template = t.render(c)
#     return HttpResponse(rendered_template)

# def detail(request):
#         return HttpResponse('got here!')
