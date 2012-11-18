#!/usr/bin/env python
# encoding=utf-8
# maintainer: Fadiga

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Ecole(models.Model):
    name = models.CharField(max_length=200)
    addresse = models.CharField(max_length=200)

    def __unicode__(self):
        return u"%s %s" % (self.name, self.addresse)


class Candidat(models.Model):

    M = "m"
    F = "f"
    SEX = ((F, u"Fille"), (M, u"Garçon"))

    ecole = models.ForeignKey(Ecole)
    last_name = models.CharField(max_length=200, verbose_name="Nom")
    first_name = models.CharField(max_length=200, verbose_name="Prénon")
    non_pere = models.CharField(max_length=200, verbose_name="Nom du père")
    surname_mother = models.CharField(max_length=200, verbose_name="Nom de la mère")
    birth_date = models.DateField(verbose_name="Date de naissance")
    sex = models.CharField(max_length=30, verbose_name=(u"Sexe"),\
                                             choices=SEX, default=F)

    def __unicode__(self):
        return u"%s %s" % (self.last_name, self.ecole)

    def cadidat_bac(self):
        return Examan.objects.filter(type_ex=Examan.B)


class Examan(models.Model):

    D = "d"
    B = "b"
    C = "c"
    BT = "bt"
    Type_op = ((D, "DEF"), (B, "BAC"), (C, "CAP"), (BT, "BT"))

    type_ex = models.CharField(max_length=30, verbose_name=(u"Examan de"),\
                                             choices=Type_op, default=B)
    candidats = models.ForeignKey(Candidat)
    num_place = models.IntegerField(verbose_name="Numero de place", unique=True)
    date_session = models.DateField(verbose_name="Session de")
    annee_scol = models.CharField(max_length=200, verbose_name=" Année scolaire")

    def __unicode__(self):
        return u"%d %s %s" % (self.num_place, self.type_ex, self.candidats.last_name)


class Question(models.Model):

    C = "cr"
    T = "tr"
    R = "re"

    STATUS = ((C, "Create"), (T, "Traitement"), (R, "Repondu"))

    question = models.TextField(verbose_name=(u"Question"))
    date = models.DateTimeField(verbose_name="Date")
    num_phone = models.CharField(max_length=20, verbose_name="Numero")
    status = models.CharField(max_length=30, verbose_name=u"Status",
                              choices=STATUS, default=C)

    def __unicode__(self):
        return u"%s %s %s %s" % (self.question, self.status, self.date,
                                 self.num_phone)

    def to_dict(self):
        return ({'question': self.question,
                 'date': self.date.strftime("%d/%m %H:%Mm"),
                 'num_phone': self.num_phone,
                 'status': self.status,
                 'id': self.id})


class Amswer(models.Model):

    user = models.ForeignKey(User, verbose_name="Utilisateur")
    texte = models.TextField(verbose_name="Reponse")
    date = models.DateTimeField(verbose_name="Date")
    question = models.ForeignKey(Question, verbose_name="Question")

    def __unicode__(self):
        return u"%s %s %s %s" % (self.question, self.reponse, self.date,
                                 self.texte)

    def to_dict(self):
        return ({'question': self.question,
                 'date': self.date.strftime("%d/%m %H:%Mm"),
                 'texte': self.texte,
                 'user': self.user,
                 'id': self.id})
