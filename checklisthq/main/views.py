import logging

from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm

from checklistdsl import lex, parse

from forms import DSLForm

_logger = logging.getLogger(__name__)

def home(request):
    """
    Simplest possible case.
    """
    form = DSLForm
    result = ''
    if request.method == 'POST':
        form = DSLForm(request.POST)
        if form.is_valid():
            raw = form.cleaned_data['specification']
            tokens = lex.get_tokens(raw)
            result = parse.get_form(tokens)

    context = {
        'form': form,
        'result': result
    }

    return render(request, 'home.html', context)

def new_user(request):
    form = UserCreationForm()
    context = {}
    context['form'] = form
    return render(request, 'registration/new_user.html', context)
