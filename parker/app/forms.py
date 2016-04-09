from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='first_name', max_length=100)