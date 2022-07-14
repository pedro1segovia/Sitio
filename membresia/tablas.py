
from django_tables2 import columns
from django_tables2.utils import A

from apps.base.tables import TablaBasica

class TablaCliente(TablaBasica):
    class Meta(TablaBasica.Meta):
        attrs = {'class': 'paleblue table' }

    documento = columns.Column(verbose_name='Documento')
    nombre = columns.Column(verbose_name='Nombre')
    apellido = columns.Column(verbose_name='Apellido')
    ver = columns.LinkColumn('product_view', text='Detalle', verbose_name='Acción', args=[A('pk')])
    accion = columns.LinkColumn('product_edit', text='Editar', verbose_name='Acción', args=[A('pk')])
    link = columns.LinkColumn('product_delete', text='Eliminar', verbose_name='Acción', args=[A('pk')])


    

   
