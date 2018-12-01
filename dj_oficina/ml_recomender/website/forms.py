from django import forms
from ml_recomender.models import Funcionario
class InsereFuncionarioForm(forms.ModelForm):
    chefe = forms.BooleanField(label='Chefe?',required=True)
    biografia = forms.CharField(label='Biografia',required=False,widget=forms.Textarea)

    class Meta:
        model = Funcionario

        #campos que estarao no forms
        fields = [
            'nome',
            'cpf',
            'remuneracao'
        ]

        exclude = [
            'tempo_de_servico'
        ]
