from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.shortcuts import render, redirect
from .models import Album
from .forms import UserForm

class IndexView(generic.ListView):
    template_name = 'homepage/index.html'
    context_object_name = 'all_albums'
    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'homepage/details.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_name', 'genre', 'album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_name', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('homepage:index')