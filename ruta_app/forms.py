from django import forms

from .models import tablaSuma, Rutas

class sumaForm(forms.ModelForm):

    class Meta:
        model = tablaSuma
        fields = ('dato1', 'dato2')

class ACOForm(forms.ModelForm):

    class Meta:
        model = Rutas
        fields = ('estacionInicio', 'estacionDestino')