from django import forms
from .models import *


class Createpost(forms.ModelForm):
    class Meta:
        model=Post
        fields="__all__"

