
from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from .models import Ciudad, Barrio
from .forms import  PruebaForm, BarrioForm
from django.views.generic import ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django_tables2 import SingleTableView
from .tablas import TablaPrueba, TablaBarrio


class ProductList(SingleTableView, ListView): 
    model = Ciudad
    template_name = 'products/tabla.html'
    table_class = TablaPrueba
    paginate_by = 2
    
class ProductDetail(DetailView): 
    model = Ciudad
    template_name = 'products/product_detail.html'
    

class ProductCreate(SuccessMessageMixin, CreateView): 
    model = Ciudad
    form_class = PruebaForm
    template_name = 'products/product_form2.html'
    success_url = reverse_lazy('product_list')
    success_message = "Product successfully created!"

class ProductUpdate(SuccessMessageMixin, UpdateView): 
    model = Ciudad
    form_class = PruebaForm
    template_name = 'products/product_form2.html'
    success_url = reverse_lazy('product_list')
    success_message = "Product successfully updated!"

class ProductDelete(SuccessMessageMixin, DeleteView):
    model = Ciudad
    template_name = 'products/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')
    success_message = "Product successfully deleted!"

######## BARRIO ############
class BarrioList(SingleTableView, ListView): 
    model = Barrio
    template_name = 'barrio/listado_barrio.html'
    table_class = TablaBarrio
    paginate_by = 3
    
class BarrioCreate(SuccessMessageMixin, CreateView): 
    model = Barrio
    form_class = BarrioForm
    template_name = 'barrio/form_barrio.html'
    success_url = reverse_lazy('barrio_list')

class BarrioUpdate(SuccessMessageMixin, UpdateView): 
    model = Barrio
    form_class = BarrioForm
    template_name = 'barrio/form_barrio.html'
    success_url = reverse_lazy('barrio_list')

class BarrioDelete(SuccessMessageMixin, DeleteView):
    model = Barrio
    template_name = 'barrio/delete_barrio.html'
    success_url = reverse_lazy('barrio_list')

