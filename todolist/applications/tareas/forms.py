from django import forms
from .models import Tareas

class TareaForm(forms.ModelForm):

    class Meta:
        model = Tareas
        fields = ['name', 'description', 'completed']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre de la tarea'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Descripcion'}),
            'completed': forms.Select(attrs={'class':'form-control'}),
        }
        labels = {
            'name':'', 'description':''
        }