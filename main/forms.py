# forms.py
from django import forms
from .models import *
 


class PostForm(forms.ModelForm):
    class Meta:
        model = Jeff
        fields = ['image',]