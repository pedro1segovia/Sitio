from django import forms
from django.core.exceptions import ValidationError

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, Button
from crispy_forms.layout import Field






class FormPadre(forms.Form):
    def __init__(self, *args, **kwargs):
        super(FormPadre, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-8'
        self.helper.form_tag = False


class BaseForm(FormPadre):
    # Campo base, si esta vacio el registro se creara, sino se actualizara
    registro_pk = forms.CharField(required=False)
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        self.custom_data = False
        self.helper.form_class = 'base-form'
        self.fields['registro_pk'].widget = forms.HiddenInput()
