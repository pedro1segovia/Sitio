from django_tables2 import columns
from django_tables2.utils import A

from tables import TablaBasica


class Secuencia(TablaBasica):

    nombre = columns.Column(verbose_name="Nombre Secuencia")
    model = columns.Column(verbose_name="Modelo")
    incremento = columns.Column(verbose_name="Incremento")
    #acciom = columns.LinkColumn('secuencia', orderable=False, text='Ver secuencia', args=[A('pk')], verbose_name='Ver registro')
    link = columns.TemplateColumn(template_name="base/boton_operar_secuencia.html", verbose_name='Operación')

    class Meta(TablaBasica.Meta):
        fields = []

