from django.shortcuts import render
from django.views.generic import ListView,UpdateView,DeleteView,CreateView,TemplateView
from ml_recomender.models import Funcionario
from website.forms import InsereFuncionarioForm
from django.urls import reverse_lazy
# Create your views here.

class IndexTemplateView(TemplateView):
    template_name = "website/index.html"

class FuncionarioListView(ListView):
    template_name = "website/lista.html"
    model = Funcionario
    context_object_name = "funcionarios" #vairavel que estará disponivel no contexto do templare

class FuncionarioUpdateView(UpdateView):
    template_name = 'atualiza.html'
    model = Funcionario
    fields = '__all__'
    context_object_name = 'funcionario'

    def get_object(self,queryset=None):
        funcionario = None

        id = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)

        if id is not None:
            funcionario = Funcionario.objects.filter(id=id).first()

        elif slug is not None:
            #pega o campo slug do model
            campo_slug = self.get_slug_field()
            # busca o funcionario aprtir do slug
            funcionario = Funcionario.objects.filter({campo_slug:slug}).first()

            return funcionario

class FuncionarioDeleteView(DeleteView):
    template_name = 'website/exclui.html'
    model = Funcionario
    success_url = reverse_lazy("website:lista_funcionarios")

class FuncionarioCreateView(CreateView):
    template_name = "website/cria.html"
    model = Funcionario
    form_class = InsereFuncionarioForm
    success_url = reverse_lazy(
        "website:lista_funcionarios"
    )
