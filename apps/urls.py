# -*- coding: utf-8 -*-
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductList.as_view(), name='product_list'),
    path('view/<int:pk>', views.ProductDetail.as_view(), name='product_view'),
    path('new', views.ProductCreate.as_view(), name='product_new'),
    path('edit/<int:pk>', views.ProductUpdate.as_view(), name='product_edit'),
    path('delete/<int:pk>', views.ProductDelete.as_view(), name='product_delete'),
]

#Barrio
urlpatterns += [
    path('barrio', views.BarrioList.as_view(), name='barrio_list'),
    path('ViewBarrio/<int:pk>', views.ProductDetail.as_view(), name='barrio_view'),
    path('NewBarrio', views.BarrioCreate.as_view(), name='barrio_new'),
    path('EditBarrio/<int:pk>', views.BarrioUpdate.as_view(), name='barrio_edit'),
    path('DeleteBarrio/<int:pk>', views.BarrioDelete.as_view(), name='barrio_delete'),
]
