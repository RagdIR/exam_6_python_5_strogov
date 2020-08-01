from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from django.utils import timezone

from .models import Guestbook
from .forms import GuestbookForm


def index_view(request):
    is_admin = request.GET.get('is_admin', None)
    if is_admin:
        data = Guestbook.objects.all()
    else:
        data = Guestbook.objects.filter(status='active')
    return render(request, 'index.html', context={
        'guestbooks': data
    })


def guestbook_create_view(request):
    if request.method == "GET":
        return render(request, 'guestbook_create.html', context={
            'form': GuestbookForm()
        })
    elif request.method == 'POST':
        form = GuestbookForm(data=request.POST)
        if form.is_valid():
            guestbook = Guestbook.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                text=form.cleaned_data['text'],
                status=form.cleaned_data['status'],
            )
            return redirect('index')
        else:
            return render(request, 'guestbook_create.html', context={
                'form': form
            })
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


def guestbook_update_view(request, pk):
    guestbook = get_object_or_404(Guestbook, pk=pk)
    if request.method == "GET":
        form = GuestbookForm(initial={
            'name': guestbook.name,
            'email': guestbook.email,
            'text': guestbook.text,
            'created_at': guestbook.created_at,
            'updated_at': guestbook.updated_at,
            'status': guestbook.status,
        })
        return render(request, 'guestbook_update.html', context={
            'form': form,
            'guestbook': guestbook
        })
    elif request.method == 'POST':
        form = GuestbookForm(data=request.POST)
        if form.is_valid():
            guestbook.name = form.cleaned_data['name']
            guestbook.email = form.cleaned_data['email']
            guestbook.text = form.cleaned_data['text']
            guestbook.status = form.cleaned_data['status']
            guestbook.save()
            return redirect('index')
        else:
            return render(request, 'guestbook_update.html', context={
                'guestbook': guestbook,
                'form': form
            })
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


def guestbook_delete_view(request, pk):
    guestbook = get_object_or_404(Guestbook, pk=pk)
    if request.method == 'GET':
        return render(request, 'guestbook_delete.html', context={'guestbook': guestbook})
    elif request.method == 'POST':
        guestbook.delete()
        return redirect('index')
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])