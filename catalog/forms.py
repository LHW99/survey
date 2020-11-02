
from django.forms.models import inlineformset_factory
from .models import Surveys, Questions, Answers

QuestionsFormset = inlineformset_factory(Surveys, Questions, fields=('question',))
AnswersFormset = inlineformset_factory(Questions, Answers, fields=('answer',))