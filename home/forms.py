from . models import *
from django import forms

class ModelForm(forms.ModelForm):
    class Meta:
        model=notes
        fields=['name','img','desc']