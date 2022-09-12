from django.shortcuts import render

# Create your views here.

##### Self #####
from django.http import HttpResponse
from . models import ToDoList, Item

def index_view(response, id): # pass in id <int>
    ls = ToDoList.objects.get(id = id)
    # return HttpResponse('<h1>%s</h1><br>%s</br>' % (ls.name, items.text)) # use int id to query ToDoList name
    context = {
        'name' : ls.name
    }
    return render(response, 'base.html')

def home_view(response):
    return render(response, 'home.html')

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