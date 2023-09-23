from django import forms

from django.forms import ModelForm


class ImageForm(forms.Form):
    image = forms.ImageField()
