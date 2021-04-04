from django import forms
from django.forms import ModelForm

from .models import *


class EntryForm(forms.ModelForm):
    category = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Category'}))
    amount = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Amount'}))
    balance = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Balance'}))

    class Meta:
        model = EntryItem
        fields = ('category', 'amount', 'balance', 'account')
        # fields = '__all__'
