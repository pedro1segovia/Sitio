from django.urls import path
from . import views


urlpatterns = [
    path('Cliente', views.ListCliente.as_view(), name='list_cliente'),
    #path('ViewCliente/<int:pk>', views.ProductDetail.as_view(), name='cliente_view'),
    path('NewCliente', views.CreateCliente.as_view(), name='new_cliente'),
    path('EditCliente/<int:pk>', views.UpdateCliente.as_view(), name='edit_cliente'),
    path('DeleteCliente/<int:pk>', views.DeleteCliente.as_view(), name='delete_cliente'),
]
