from django import forms


class NameForm(forms.Form):

    firstname = forms.CharField(label='Your first name', max_length=100)
    surname = forms.CharField(label='Your surname', max_length=100)
    birthdate = forms.DateField(label='Birth date',input_formats=['%d-%m-%Y'])
