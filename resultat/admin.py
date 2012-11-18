#!/usr/bin/env python
# encoding=utf-8
# maintainer: Fadiga


from django.contrib import admin

from models import (Candidat, Examan, Ecole, Question, Amswer)


class EcoletAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'name', 'addresse')


class CandidatAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'first_name', 'last_name', 'sex',\
                        'surname_mother', 'birth_date', 'ecole')


class ExamanAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'num_place', 'type_ex',
                    'date_session', 'annee_scol')


class AmswerAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'user', 'date',
                    'question', 'texte')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'date', 'question',
                    'num_phone', 'status')
    fieldsets = [
        (None,               {'fields': ['date']}),
        (u'Numéro de téléphone', {'fields': ['num_phone']}),
        ('Question', {'fields': ['question']}),
        ('None', {'fields': ['status']}),
    ]


admin.site.register(Examan, ExamanAdmin)
admin.site.register(Ecole, EcoletAdmin)
admin.site.register(Candidat, CandidatAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Amswer, AmswerAdmin)
