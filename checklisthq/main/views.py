import logging

from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from checklistdsl import lex, parse

from forms import DSLForm, NewUserForm

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
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            user = User.objects.create_user(username, email, password)
    else:
        form = NewUserForm()
    context = {}
    context['form'] = form
    return render(request, 'registration/new_user.html', context)
