from django.urls import reverse_lazy
from django.shortcuts import render

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView
)

from .models import Cliente

class ClienteList(ListView):
    model = Cliente
    queryset = Cliente.objects.all()
    template_name = 'cliente/cliente_lista.html'


class ClienteCreate(CreateView):
    model = Cliente
    fields = '__all__'
    template_name = 'cliente/cliente_cadastro.html'
    success_url = reverse_lazy('loja_app:cliente')


class ClienteUpdate(UpdateView): 
    model = Cliente
    fields = '__all__'
    template_name = 'cliente/cliente_cadastro.html'
    success_url = reverse_lazy('loja_app:cliente')


class ClienteDetail(DetailView): 
    model = Cliente
    #queryset = Cliente.objects.all()
    template_name = 'cliente/cliente_detail.html'


class ClienteDelete(DeleteView):
    model = Cliente
    template_name = 'cliente/cliente_confirm_delete.html'
    success_url = reverse_lazy('loja_app:cliente')