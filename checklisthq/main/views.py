import logging

from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from checklistdsl import lex, parse

from forms import ChecklistForm, NewUserForm
from models import Checklist

_logger = logging.getLogger(__name__)

def home(request):
    """
    Simplest possible case.
    """
    return render(request, 'frontpage.html')

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

def checklist_list(request, username):
    context = {}
    try:
        owner = User.objects.get(username=username)
    except User.DoesNotExist:
        # TODO: Return a 404 when we've configured it.
        return HttpResponseRedirect('/')
    checklists = Checklist.objects.filter(owner=owner).order_by('-modified')
    is_own_checklists = owner == request.user
    context['checklists'] = checklists
    context['is_own_checklists'] = is_own_checklists
    context['owner'] = owner
    return render(request, 'user/checklist_list.html', context)

def new_checklist(request):
    """
    Creates a new checklist.
    """
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    form = ChecklistForm()
    context = {}
    if request.method == 'POST':
        form = ChecklistForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            user = request.user
            checklist = Checklist.objects.create(
                title=title,
                content=content,
                owner=user
            )
            context['saved'] = True
    context['form'] = form
    context['action'] = '/checklist/new'
    return render(request, 'user/edit_checklist.html', context)

def view_checklist(request, id):
    checklist = Checklist.objects.get(id=id)
    tokens = lex.get_tokens(checklist.content)
    result = parse.get_form(tokens)
    context = {
        'checklist': checklist,
        'result': result
    }
    return render(request, 'view_checklist.html', context)

def edit_checklist(request, id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    checklist = Checklist.objects.get(id=id)
    if not checklist.owner == request.user:
        return HttpResponseRedirect('/')
    context = {}
    if request.method == 'POST':
        form = ChecklistForm(request.POST, instance=checklist)
        if form.is_valid():
            form.save()
            context['saved'] = True
    else:
        form = ChecklistForm(instance=checklist)
    context['action'] = '/checklist/%s/edit' % id
    context['form'] = form
    return render(request, 'user/edit_checklist.html', context)
