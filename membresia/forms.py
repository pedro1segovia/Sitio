from django import forms
from .models import Cliente
from django.forms.widgets import NumberInput
from django.forms import Form, ModelForm, TextInput
from crispy_forms.layout import Layout, Div, Fieldset, Row, Column
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ClienteForm(forms.ModelForm):
    fecha_nacimiento = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    fecha_ingreso = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    class Meta:
            model = Cliente
            fields = ['documento', 'nombre', 'apellido', 'direccion', 'contacto',
            'correo_electronico', 'genero', 'fecha_nacimiento', 'fecha_ingreso']
    
            
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Fieldset('direccion', css_class='form-group col-md-6 mb-0'),
                Fieldset('contacto', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'))
        
        
        
        