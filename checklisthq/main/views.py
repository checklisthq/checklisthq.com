import logging

from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from checklistdsl import lex, parse

from forms import ChecklistForm, NewUserForm
from models import Checklist

_logger = logging.getLogger(__name__)

def home(request):
    """
    Simplest possible case.
    """
    if request.user.is_authenticated():
        return HttpResponseRedirect('/user/%s' % request.user.username)
    else:
        return render(request, 'frontpage.html')

def new_user(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            user = User.objects.create_user(username, email, password)
            u = authenticate(username=username, password=password)
            login(request, u)
            return HttpResponseRedirect('/user/%s' % username)
    else:
        form = NewUserForm()
    context = {}
    context['form'] = form
    return render(request, 'registration/new_user.html', context)

def browse(request):
    context = {}
    checklists = Checklist.objects.all
    context['checklists'] = checklists
    return render(request, 'checklist_browse.html', context)

def checklist_list(request, username):
    context = {}
    try:
        owner = User.objects.get(username=username)
    except User.DoesNotExist:
        # TODO: Return a 404 when we've configured it.
        return HttpResponseRedirect('/')
    checklists = Checklist.objects.filter(owner=owner).order_by('-modified')
    context['checklists'] = checklists
    context['is_own_checklists'] = owner == request.user
    context['owner'] = owner
    return render(request, 'user/checklist_list.html', context)

def new_checklist(request):
    """
    Creates a new checklist.
    """
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    form = ChecklistForm()
    context = {}
    context['action'] = '/checklist/new'
    if request.method == 'POST':
        form = ChecklistForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            tags = form.cleaned_data['tags']
            user = request.user
            checklist = Checklist.objects.create(
                title=title,
                content=content,
                owner=user
            )
            checklist.tags.add(*tags)
            context['saved'] = "Your changes have been saved..."
            context['action'] = '/checklist/%s/edit' % checklist.id
    context['form'] = form
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

def checklist_comments(request, id):
    checklist = Checklist.objects.get(id=id)
    context = { 'checklist': checklist }
    return render(request, 'checklist_comments.html', context)

def edit_checklist(request, id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    checklist = Checklist.objects.get(id=id)
    if not checklist.owner == request.user:
        return HttpResponseRedirect('/')
    context = {}
    if request.method == 'POST':

		form = ChecklistForm(request.POST, instance=checklist)
		if 'Save' in request.POST:
			if form.is_valid():
				form.save()
				context['saved'] = "Your changes have been saved..."
		if 'Preview' in request.POST:
			if form.is_valid():
				content = form.cleaned_data['content']
				tokens = lex.get_tokens(content)
				result = parse.get_form(tokens)
				context = {
					'checklist': checklist,
					'result': result
				}
				return render(request, 'view_checklist.html', context)
    else:
        form = ChecklistForm(instance=checklist)
    context['action'] = '/checklist/%s/edit' % id
    context['form'] = form
    return render(request, 'user/edit_checklist.html', context)

def clone_checklist(request, id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    old = Checklist.objects.get(id=id)
    checklist = Checklist.objects.create(
        title=old.title,
        content=old.content,
        owner=request.user,
    )
    form = ChecklistForm(instance=checklist)
    context = {}
    context['action'] = '/checklist/%s/edit' % checklist.id
    context['form'] = form
    context['saved'] = "You have copied this checklist. Edit your version below."
    return render(request, 'user/edit_checklist.html', context)

def delete_checklist(request, id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    checklist = Checklist.objects.get(id=id)
    if not checklist.owner == request.user:
        return HttpResponseRedirect('/')
    checklist.delete()
    context = { 'saved': "You have deleted this checklist." }
    return HttpResponseRedirect('/')

def search(request):
    query = request.REQUEST["query"]
    tags = [t.strip() for t in query.split(",")]
    tagged_checklists = Checklist.objects.filter(tags__name__in=tags).distinct()
    matched_checklists = Checklist.objects.filter(title__icontains=query.strip())
    checklists = [checklist for checklist in tagged_checklists]
    checklists.extend([checklist for checklist in matched_checklists])
    context = { 'checklists': checklists, 'tags': ', '.join(tags) }
    return render(request, 'search_checklist.html', context)

def print_checklist(request, id):
    checklist = Checklist.objects.get(id=id)
    modified = checklist.modified
    tokens = lex.get_tokens(checklist.content)
    result = parse.get_form(tokens)
    context = {
        'checklist': checklist,
        'result': result,
        'modified': modified,
        'username': checklist.owner.username
    }
    return render(request, 'print_checklist.html', context)

@csrf_exempt
def preview_checklist(request):
    """
    Takes a request from the markitup editor and returns a preview.
    """
    result = ''
    if request.method == 'POST':
        if 'data' in request.POST:
            raw_data = request.POST['data']
            tokens = lex.get_tokens(raw_data)
            result = parse.get_form(tokens)
    return render(request, 'preview.html', {'content': result})
