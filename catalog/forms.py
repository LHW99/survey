
from django.forms.models import inlineformset_factory
from django.forms import ModelForm
from django import forms
from .models import Surveys, Questions, Answers

QuestionsFormset = inlineformset_factory(Surveys, Questions, fields=('question',), extra=1)
AnswersFormset = inlineformset_factory(Questions, Answers, fields=('answer',), extra=4)

class SurveysForm(ModelForm):
  class Meta: 
    model = Surveys
    fields = ['name',]

class QuestionsForm(ModelForm):
  class Meta: 
    model = Questions
    fields = '__all__'

class AnswersForm(ModelForm):
  class Meta:
    model = Answers
    fields = '__all__'