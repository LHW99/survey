import datetime

from django.shortcuts import render
from django.views import generic
from catalog.models import Answers, Questions, Surveys
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def index(request):
  return render(request, 'index.html')

class SurveysListView(generic.ListView):
  model = Surveys
  paginate_by = 10

class SurveysDetailView(generic.DetailView):
  model = Surveys

class QuestionsView(generic.View):
  model = Questions

class UserSurveys(LoginRequiredMixin, generic.ListView):
  model = Surveys
  template_name = 'catalog/user_surveys_list.html'
  paginate_by = 10

  def get_queryset(self):
    return Surveys.objects.filter(survey_taker=self.request.user)