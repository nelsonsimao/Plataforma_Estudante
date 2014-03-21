# # -*- coding: utf-8 -*-
from django.db import models
import datetime
from django.utils import timezone


# Create your models here.
class OfereceBoleia(models.Model):
    descricaoOferece = models.CharField('Descrição', max_length=500)
    origemOferece = models.CharField('Origem', max_length=50)
    destinoOferece = models.CharField('Destino', max_length=50)
    dia = models.CharField('Data da viagem', max_length=50)
    hora = models.CharField('Hora da viagem', max_length=50)
    lugaresOferece = models.IntegerField('Lugares', default=1)
    custo = models.IntegerField('Preço', default=0)
    tipo_combustivel = models.CharField('Tipo de Combustível', max_length=25)
    pub_data = models.DateTimeField(default=datetime.datetime.now())
    userNameC = models.ForeignKey('accounts.MyProfile')



    def __unicode__(self):
        return self.descricaoOferece

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


#    def data(self):
#        return self.dia_hora >= timezone.now() - datetime.timedelta(days=1)



