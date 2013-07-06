from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import Textarea

from models import Checklist

class ChecklistForm(forms.ModelForm):
    """
    A form for entering the specification of a checklist.
    """
    class Meta:
        model = Checklist
        fields = ('title', 'description', 'content', 'tags')
        widgets = {
            'description': Textarea(attrs={'rows': 2, 'style': 'width:100%;',
                'class': 'input-xlarge'}),
            'content': Textarea(attrs={'rows': 16, 'style': 'width:100%;',
                'class': 'input-xlarge'}),
        }

class NewUserForm(UserCreationForm):
    email = forms.EmailField(
        label='Your email address'
    )
