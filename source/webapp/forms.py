from django import forms
from .models import STATUS_CHOICES, DEFAULT_STATUS


class GuestbookForm(forms.Form):
    name = forms.CharField(max_length=200, required=True, label='Имя')
    email = forms.CharField(max_length=30, required=True, label='Эл. почта')
    text = forms.CharField(max_length=2000, required=True, label='Текст', widget=forms.Textarea)
    status = forms.ChoiceField(choices=STATUS_CHOICES, initial=DEFAULT_STATUS, label='Статус')
