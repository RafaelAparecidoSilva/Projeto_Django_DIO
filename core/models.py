from django.db import models

#  Importamos o User do sistema para utilizar os dados dos usuários que registramos no admin do django
#  (desta forma não precisamos criar uma tabela específica no models para representar os usuários).
from django.contrib.auth.models import User
from datetime import datetime


class Evento(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Título')
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='Data de Criação')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) # CASCADE -> caso USER deletado, tudo dele será deletado do sistema.

    class Meta:
        db_table = 'evento'  # Configurando o nome da tabela no banco de dados

    # def __str__(self):  # Tratando a apresentação do objeto
    #     return self.titulo

    def get_data_evento(self):  # Conseguimos colocar uma função no models para ser utilizado pelo objeto no html
        return self.data_evento.strftime('%d/%m/%Y - %H:%Mh')

    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')

    def get_evento_atrasado(self):
        if self.data_evento < datetime.now():
            return True
        else:
            return False
