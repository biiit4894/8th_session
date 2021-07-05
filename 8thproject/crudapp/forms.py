from django import forms
from .models import Crudapp

class PostForm(forms.ModelForm):
    class Meta:
        model = Crudapp
        fields = ['title', 'body', 'pub_date']
        widgets = {
            'pub_date' : forms.DateInput(
                attrs = {
                    'class' : 'form-control',
                    'type' : 'date'
                }
            )
        }