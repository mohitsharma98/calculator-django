from django import forms


class CalForm(forms.Form):
    name = forms.CharField()
    number = forms.IntegerField()