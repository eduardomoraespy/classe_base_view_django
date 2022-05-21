from django import forms

from loja_app.models import Cliente


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'