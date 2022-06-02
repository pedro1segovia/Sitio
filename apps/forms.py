from django import forms
from .models import Ciudad, Barrio
from django.forms import Form, ModelForm, TextInput
from crispy_forms.layout import Layout, Div, Fieldset, Row, Column
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class PruebaForm(forms.ModelForm):
    class Meta:
            model = Ciudad
            fields = ['ciudad']
            
    def __init__(self, *args, **kwargs):
        #super(PruebaForm, self).__init__(*args, **kwargs)
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        
class BarrioForm(forms.ModelForm):
    class Meta:
            model = Barrio
            fields = ['barrio']
            
    def __init__(self, *args, **kwargs):
        #super(PruebaForm, self).__init__(*args, **kwargs)
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        
        


       
    

    