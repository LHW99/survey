import datetime

from django.shortcuts import render
from django.views import generic
from catalog.models import Answers, Questions, Surveys
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

from django.forms.models import inlineformset_factory
QuestionsFormset = inlineformset_factory(Surveys, Questions, fields=('question',))

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

class SurveysCreate(LoginRequiredMixin, CreateView):
  model = Surveys
  fields = ['name',]

  def get_context_data(self, *args, **kwargs):
    data = super().get_context_data(**kwargs)
    if self.request.POST:
      data['question'] = QuestionsFormset(self.request.POST)
    else:
      data['question'] = QuestionsFormset()
    return data
  
  def form_valid(self, form):
    context = self.get_context_data()
    question = context['question']
    self.object = form.save()
    if question.is_valid():
      question.instance = self.object
      question.save()
    return super().form_valid(form)
  
  def form_valid(self,form):
    surveyer = self.request.user
    form.instance.surveyer = surveyer
    return super(SurveysCreate, self).form_valid(form)

  def get_success_url(self):
    return reverse('surveys:list')

class SurveysUpdate(LoginRequiredMixin, UpdateView):
  model = Surveys
  fields = ['name',]
  template_name = 'surveys_update.html'

class SurveysDelete(LoginRequiredMixin, DeleteView):
  model = Surveys
  success_url = reverse_lazy('user-surveys')