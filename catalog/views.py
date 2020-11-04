import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from catalog.models import Answers, Questions, Surveys
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .forms import QuestionsFormset, AnswersFormset, SurveysForm, QuestionsForm, AnswersForm

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
  template_name = 'surveys_form.html'

  def post(self, request):
    form = SurveysForm(request.POST)
    if form.is_valid():
      survey = form.save(commit=False)
      survey.surveryer = request.user
      return redirect('surveys-create2', pk=survey.id)
    else:
      form = SurveysForm()
    return render(request, 'surveys_form.html', {'form': form})

class SurveysCreate2(LoginRequiredMixin, UpdateView):
  model = Questions
  fields = ('question',)
  template_name = 'surveys_form2.html'

  def get_context_data(self, *args, **kwargs):
    data = super().get_context_data(**kwargs)
    if self.request.POST:
      data['answer'] = AnswersFormset(self.request.POST)
    else:
      data['answer'] = AnswersFormset()
    return data
  
  def form_valid(self, form):
    context = self.get_context_data()
    answer = context['answer']
    self.object = form.save()
    if answer.is_valid():
      answer.instance = self.object
      answer.save()
    return super().form_valid(form)

class SurveysUpdate(LoginRequiredMixin, UpdateView):
  model = Surveys
  fields = ('name',)
  template_name = 'surveys_update.html'

class SurveysDelete(LoginRequiredMixin, DeleteView):
  model = Surveys
  success_url = reverse_lazy('user-surveys')