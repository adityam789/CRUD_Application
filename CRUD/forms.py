from django import forms
from CRUD.models import crudst

class stform(forms.ModelForm): 
    class Meta:
        model=crudst
        fields="__all__"