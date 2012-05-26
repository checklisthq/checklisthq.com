from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import Textarea

from models import Checklist

class ChecklistForm(forms.ModelForm):
    """
    A form for entering the specification of a checklist.
    title = forms.CharField(
    specification = forms.CharField(
        label='',
        initial='',
        widget=forms.Textarea(attrs={
        'class': 'input-xlarge',
        'style': 'width: 100%',
        'rows': 20})
    )"""
    class Meta:
        model = Checklist
        fields = ('title', 'content')
        widgets = {
            'content': Textarea(attrs={'rows': 16, 'style': 'width:100%;',
                'class': 'input-xlarge'}),
        }

class NewUserForm(UserCreationForm):
    email = forms.EmailField(
        label='Your email address'
    )
