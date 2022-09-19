from django import forms 


class CreateNewList(forms.Form):
    name = forms.CharField(label = 'Name', max_length = 200) # label is like label in GUI
    check = forms.BooleanField(required = False) # Check button that can be empty


