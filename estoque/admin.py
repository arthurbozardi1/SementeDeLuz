from django.contrib import admin
from .models import Cadastro, Funcionario,Integrante,Roupa,Roupacama,Alimento,Higiene

# Register your models here.
admin.site.register(Cadastro)
admin.site.register(Integrante)
admin.site.register(Roupa)
admin.site.register(Alimento)
admin.site.register(Higiene)
admin.site.register(Roupacama)
admin.site.register(Funcionario)