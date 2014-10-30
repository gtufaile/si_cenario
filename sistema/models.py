# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


STATUS_CHOICE = (
    ("em_dia", "Em dia"),
    ("atrasado", "Atrasado"),
    )

ETAPA_CHOICE = (
    ("analise_tecnica", "Analise Tecnica"),
    ("finalizado", "Finalizado"),
    ("planejamento", "Planejamento"),
    ("execucao", "Execucao"),
    ("suporte_tecnico", "Suporte Tecnico"),
    )


class Projeto(models.Model):
    nome = models.CharField("Nome", max_length=50)
    data_de_inicio = models.DateField()
    status = models.CharField("Status", max_length=50, choices=STATUS_CHOICE)
    etapa = models.CharField("Etapa", max_length=50, choices=ETAPA_CHOICE)
    # membro = models.ManyToManyField(Membro)
    descricao = models.TextField()


    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"

    def __unicode__(self):
        return self.nome

