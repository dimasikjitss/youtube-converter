from django.forms import Form
from django import forms
from .models import Link

class LinkForm(forms.Form):
    url = forms.URLField( widget=forms.TextInput(attrs={
        'placeholder': 'Enter url video from youtube.com'}))
  
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Введите свой email'}))



    class Meta:
        model = Link
        fields = '__all__'