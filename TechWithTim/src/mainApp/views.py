from django.shortcuts import render

# Create your views here.

##### Self #####
from django.http import HttpResponse, HttpResponseRedirect
from . models import ToDoList, Item
from . forms import CreateNewList

def index_view(response, id): # pass in id <int>
    ls = ToDoList.objects.get(id = id)
    # return HttpResponse('<h1>%s</h1><br>%s</br>' % (ls.name, items.text)) # use int id to query ToDoList name
    context = {
        'name' : ls.name,
        'ls' : ls
    }
    return render(response, 'list.html', context)

def home_view(response):
    return render(response, 'home.html', {})

def create_view(response): # used to create a form in html
    if response.method == 'POST':
        form = CreateNewList(response.POST) # need this when you are sending info to or from website
        
        if form.is_valid():
            n = form.cleaned_data['name'] # clean user-submitted data and unencypt
            t = ToDoList(name = n) # create new to-do list with user input name
            t.save() # save the name

        return HttpResponseRedirect('/%i' % t.id) # redirect page to newly created list
    else:
        form = CreateNewList()
    return render(response, 'form.html', {'form' : form})

# queries
# from mainApp import ToDoList, Item
# t = ToDoList.objects
# t.all()
# t.item_set()
# t.filter(keyword = '')
# del_object = t.get(id = 1)
# del_object.delete()
# t1 = ToDoList(name = 'Bo')
# t1.save()