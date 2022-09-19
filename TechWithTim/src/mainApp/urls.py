# this user-created urls.py file is used to redirect url extensions after the index/ extension

from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.index_view, name = 'index'), # <int:id> looks for some int in path, and pass that to views.index_view
    path('', views.home_view, name = 'home'),
    path('create/', views.create_view, name = 'create')
]