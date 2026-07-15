from django import forms
from .models import Tache

class TacheForm(forms.ModelForm):
    class Meta:
        model = Tache
        fields = ['titre', 'description', 'date_echeance', 'categorie']
        widgets = {
            'date_echeance': forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',
                    'class': 'w-full p-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500'
                    }
                
            ),
            'description': forms.Textarea(
                attrs={
                    'rows': 3,
                    'class': 'w-full p-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500'
                    }
            ),
            'titre': forms.TextInput(
                attrs={
                    
                    'class': 'w-full p-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500'
                    }
            )
            # 'categorie': forms.Textarea(
            #     attrs={
                    
            #         'class': 'w-full p-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500'
            #         }
            # )
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
           
            self.fields['categorie'].widget.attrs.update({
                'class': 'w-full p-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500'
            })