from pyexpat import model
from django.forms import ModelForm
from .models import Cadastro

class CadastroForm(ModelForm):
    class Meta:
        model = Cadastro
        fields = ['nome', 'sobrenome', 'idade','nascimento', 'descricao']