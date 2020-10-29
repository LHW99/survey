import datetime

from django.shortcuts import render
from django.views import generic
from catalog.models import Answers, Questions, Surveys
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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
    return Surveys.objects.filter(surveyer=self.request.user)

class SurveysCreate(CreateView):
  model = Surveys
  fields = '__all__'

class SurveysUpdate(UpdateView):
  model = Surveys
  fields = '__all__'

class SurveysDelete(DeleteView):
  model = Surveys
  success_url = reverse_lazy('user-surveys')