from django.contrib import admin

# Register your models here.

# self-defined
from . models import ToDoList, Item # import the models you want
admin.site.register(ToDoList) # register and allow ToDoList to populate on admin site
admin.site.register(Item)
