import datetime

from django.shortcuts import render
from django.views import generic
from catalog.models import Answers, Questions, Surveys

# Create your views here.

def index(request):
  return render(request, 'index.html')

class SurveyListView(generic.ListView):
  model = Surveys
  paginate_by = 10

class SurveyDetailView(generic.DetailView):
  model = Surveys

