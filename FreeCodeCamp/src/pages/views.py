from django.http import HttpResponse # allows to render(?) html string into HTTP response
from django.shortcuts import render

# Create your views here.


# Handle webpages
def home_view(request, *args, **kwargs):
    '''
    request : request from user that is accessing to page
    args : shows default args getting pasted in
    '''
    # print(args, kwargs)
    # return HttpResponse("<h1>Hello World!</h1>")
    return render(request, 'home.html', {}) # request, html rendering, context

def contact_view(request, *args, **kwargs):
    return HttpResponse('<h1>Contact Views</h1>')

def about_view(request, *args, **kwargs):
    my_context = {
        'my_text' : 'this is about us',
        'my_number' : '1919191',
        'my_list' : [12, 113, 3243]
    }
    return render(request, 'about.html', my_context)