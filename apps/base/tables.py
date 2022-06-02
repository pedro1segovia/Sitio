from __future__ import print_function
import os

from django.apps import apps

from django_tables2 import tables, columns
from django_tables2.config import RequestConfig
from django_tables2.utils import AttributeDict

from django.utils.html import format_html

# Super clase de tablas
# Agrega contador, clase css por defecto, desactiva ordenación y data-id de la fila


class TablaBasica(tables.Table):
    counter = columns.TemplateColumn("{{row_counter}}", verbose_name='#')
    # counter = columns.TemplateColumn("{{row_counter|add:table.page.start_index}}", verbose_name='#')

    class Meta:
        template_name = 'django_tables2/bootstrap4.html'
        attrs = {"class": "paleblue"}
        orderable = False
        lambda record: print(type(record))
        # row_attrs = {"data-id": lambda record: record.pk}
        row_attrs = {"data-id": lambda record: record.pk if type(record) != dict else None}


class TablaSeleccionable(TablaBasica):
    selection = columns.CheckBoxColumn(accessor='id')

    class Meta(TablaBasica.Meta):
        attrs = {"class": "paleblue seleccionable"}


class MovimientosTablaBase(TablaBasica):

    class Meta(TablaBasica.Meta):
        pass

    matricula = columns.Column(accessor='matricula', verbose_name='Matrícula')
    socio = columns.Column(accessor='socio', verbose_name='Socio')
    tipo = columns.Column(accessor='tipo', verbose_name='Tipo')
    numero = columns.Column(accessor='numero', verbose_name='Número')
    fecha = columns.Column(accessor='fecha', verbose_name='Fecha')
    concepto = columns.Column(accessor='concepto', verbose_name='Concepto')
    monto = columns.Column(accessor='importe', verbose_name='Importe', attrs={"td": {'class': 'table-numeric'}})



class FixedFileColumn(columns.FileColumn):

    def render(self, record, value):
        storage = getattr(value, 'storage', None)
        exists = None
        url = None
        if storage:
            # we'll assume value is a `django.db.models.fields.files.FieldFile`
            if self.verify_exists:
                exists = storage.exists(value.name)
            url = '/static/' + storage.url(value.name)

        else:
            if self.verify_exists and hasattr(value, 'name'):
                # ignore negatives, perhaps the file has a name but it doesn't
                # represent a local path... better to stay neutral than give a
                # false negative.
                exists = os.path.exists(value.name) or exists

        tag = 'a' if url else 'span'
        attrs = AttributeDict(self.attrs.get(tag, {}))
        attrs['title'] = value.name
        attrs['target'] = 'blank'

        classes = [c for c in attrs.get('class', '').split(' ') if c]
        if exists is not None:
            classes.append('exists' if exists else 'missing')
        attrs['class'] = ' '.join(classes)

        if url:
            return self.render_link(url, record=record, value=value, attrs=attrs)
        else:
            return format_html(
                '<span {attrs}>{text}</span>',
                attrs=attrs.as_html(),
                text=self.text_value(record, value)
            )

    
