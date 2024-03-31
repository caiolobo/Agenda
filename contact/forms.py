from typing import Any, Mapping
from django import forms
from django.core.exceptions import ValidationError
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from contact.models import Contact



class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'classe-a classe-b',
                'placeholdet': 'Veio do Init'
            }
        ),
        label='Primeiro None',
        help_text='Texto de apoio',
    )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['first_name'].widget.attrs.update({
        #     'class':'classe-a',
        #     'placeholder':'Escreva aqui'
        # })


    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone',)
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class':'classe-a',
        #             'placeholder':'Escreva aqui'
        #         }
        #     )
        # }

    def clean(self):
        # cleaned_data = self.cleaned_data

        # self.add_error(
        #     'first_name',
        #     ValidationError(
        #         'MEnsagem de erro',
        #         code='invalid'
        #     )
        # )

        return super().clean()
    
    # def clean_first_name(self):
    #     first_name = self.cleaned_data.get('first_name'):
    #     return first_name