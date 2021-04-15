from django import forms
from django.forms import ModelForm

from .models import *


class EntryForm(forms.ModelForm):
    category = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Category','id':'id_category'}))
    amount = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Amount', 'id':'id_amount'}))

    class Meta:
        model = EntryItem
        fields = ('category', 'amount', 'account')
        # fields = '__all__'
