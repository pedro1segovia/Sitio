from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import  ClienteForm
from django.views.generic import ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django_tables2 import SingleTableView
from .tablas import TablaCliente


class ListCliente(SingleTableView, ListView): 
    model = Cliente
    template_name = 'cliente/listado_cliente.html'
    table_class = TablaCliente
    paginate_by = 10
    
# class ProductDetail(DetailView): 
#     model = Ciudad
#     template_name = 'products/product_detail.html'

class CreateCliente(SuccessMessageMixin, CreateView): 
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/form_cliente.html'
    success_url = reverse_lazy('list_cliente')

class UpdateCliente(SuccessMessageMixin, UpdateView): 
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/form_cliente.html'
    success_url = reverse_lazy('list_cliente')

class DeleteCliente(SuccessMessageMixin, DeleteView):
    model = Cliente
    template_name = 'cliente/delete_cliente.html'
    success_url = reverse_lazy('list_cliente')
