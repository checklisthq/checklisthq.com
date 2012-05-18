from django import forms

class DSLForm(forms.Form):
    """
    A form for entering the specification of a checklist.
    """
    specification = forms.CharField(widget=forms.Textarea())
