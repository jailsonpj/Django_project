from django.urls import path
from website.views import FuncionarioListView,FuncionarioUpdateView,FuncionarioDeleteView,FuncionarioCreateView,IndexTemplateView

app_name = 'website'

#urlpatterns contém a lista de roteamento de urls
urlpatterns = [
    #GET/
    path('',IndexTemplateView.as_view(),name='index'),

    path('funcionarios/',FuncionarioListView.as_view(),
    name='lista_funcionarios'),

    path('funcionario/<pk>',
        FuncionarioUpdateView.as_view(),
        name='atualiza_funcionario'),

    path('funcionario/excluir/<pk>',
        FuncionarioDeleteView.as_view(),
        name='deleta_funcionario'),

    path('funcionario/cadastrar/',
        FuncionarioCreateView.as_view(),
        name ='cadastra_funcionario'),
]
