#from msilib.schema import ListView
from turtle import home
from django.shortcuts import render, redirect
from estoque.models import Cadastro, Funcionario
from django.views.generic.edit import CreateView, FormView
from django.views.generic.list import ListView
from django.views.generic import DetailView
from estoque.models import Alimento, Higiene, Integrante, Roupa, Roupacama, Integrante, Funcionario, Cadastro
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from estoque.forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import TemplateView

 
class LanguageView(TemplateView):
    template_name ='language.html'

class OpcaoCadastroView(TemplateView):
    template_name ='opcao-cadastro.html'
    
class EstoqueCategoriasView(TemplateView):
    template_name ='language.html'

class OpcaoVerCadastroView(TemplateView):
    template_name ='opcao_ver_cadastro.html'

class OpcaoVerEstoqueView(TemplateView):
    template_name ='opcao_ver_estoque.html'
 
class OpcaoPessoasView(TemplateView):
    template_name ='cadastro_pessoas.html'   

class CategoriasCadastroView(TemplateView):
    template_name ='categorias_cadastro.html'

class OpcaoView(TemplateView):
    template_name ='opcao_ver_estoque.html' 
    
class OpcaoEstoqueView(TemplateView):
    template_name ='opcao_estoque.html'

class EscolhaView(TemplateView):
    template_name ='escolha.html'
    
 
def CadastroView(request):
    if request.user.is_authenticated:
        return redirect ('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                
                Cadastro.objects.create(usuario=user,)
                messages.success(request, 'Usuário criado com sucesso: ' + username)
                return redirect('login')
        
        context = {'form' : form}
        return render (request, 'cadastro.html', context)
    
def loginPage(request):
    if request.user.is_authenticated:
        return redirect ('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username= username, password=password)
            
            if user is not None:
                login(request, username)
                return redirect('home')
            else:
                messages.info(request, 'O usuário ou a senha está incorreto')
                    
        context = {}
        return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def userPage(request):
    orders = request.user.order_set.all()
    print('ORDERS: ', orders)
    context = {'orders': orders}
    return render(request, 'estoque/perfil.html',context)

class AddRoupaView(CreateView): 
    model = Roupa
    fields = ['tipos', 'cor', 'qntd', 'tamanho', 'condicao']
    template_name = 'add_roupas.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class AddRoupaCamaView(CreateView):
    model = Roupacama
    fields = ['tipos', 'descr', 'cor','qntd', 'tamanho', 'condicao']
    template_name = 'add_roupacama.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class AddHigieneView(CreateView):
    model = Higiene
    fields = ['tipos', 'descr', 'qntd', 'vencimento']
    template_name = 'add_higiene.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class AddIntegranteView(CreateView):
    model = Integrante
    fields = ['nome', 'email', 'telefone', 'dt_ingresso','dt_nasct','cpf']
    template_name = 'add_visitantes.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class AddAlimentoView(CreateView):
    model = Alimento
    fields = ['tipos', 'descr', 'qntd', 'vencimento']
    template_name = 'add_comida.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class AddFuncionarioView(CreateView):
    model = Funcionario
    fields = ['nome', 'email', 'dt_ingresso', 'dt_nasct','cpf','telefone','cep','endereco','sexo']
    template_name = 'add_funcionarios.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    


class VerRoupaView(ListView):
    model= Roupa
    template_name = 'ver_roupas.html'
    
class VerRoupaCamaView(ListView):
    model= Roupacama
    template_name = 'ver_roupacama.html'
    
class VerHigieneView(ListView):
    model= Higiene
    template_name = 'ver_higiene.html'
    
class VerAlimentoView(ListView):
    model= Alimento
    template_name = 'ver_comida.html'

class VerIntegranteView(ListView):
    model= Integrante
    template_name = 'ver_visitantes.html'


class VerFuncionarioView(ListView):
    model= Funcionario
    template_name = 'ver_funcionarios.html'



    