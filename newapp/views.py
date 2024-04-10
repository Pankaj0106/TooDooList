from django.shortcuts import render
from newapp.forms import user_form
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from newapp.models import user_model
from django.urls import reverse_lazy
# Create your views here.

class home(ListView):
    template_name='index.html'
    model = user_model
    context_object_name = 'list'
    

class CreateListView(CreateView):
    template_name='newapp/list.html'
    form_class = user_form
    success_url = '/'


class UpdateListView(UpdateView):
    template_name = 'newapp/update.html'
    model = user_model
    fields = ('__all__')
    success_url = reverse_lazy('home')

class DeleteListView(DeleteView):
    model = user_model
    template_name ='newapp/delete.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('home')
