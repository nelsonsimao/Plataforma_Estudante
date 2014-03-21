# -*- coding: UTF-8 -*-
from django.db import models
import datetime
from django.utils import timezone


# Create your models here.
class AlugoCasa(models.Model):
    descricao = models.CharField('Descrição', max_length=500)
    bairro = models.CharField('Bairro', max_length=50)
    quartos = models.IntegerField('Quartos', default=1)
    sala = models.CharField('Sala', max_length=5)
    wc = models.IntegerField('Casa de banho', default=1)
    renda = models.IntegerField('Renda por mês', default=0)
    animais = models.CharField('Animais', max_length=5)
    genero = models.CharField('Género', max_length=15)
    mes = models.CharField('Disponível em', max_length=15)
    pub_data = models.DateTimeField(default=datetime.datetime.now())
    userName = models.ForeignKey('accounts.MyProfile')


    def __unicode__(self):
        return self.descricao

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

