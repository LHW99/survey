from django.urls import path
from . import views
from django.urls import include
from django.views.generic import RedirectView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', views.index, name='index')
]

urlpatterns += [
  path('surveys/', views.SurveyListView.as_view(), name='survey-list'),
  path('surveys/<int:pk>/', views.SurveyDetailView.as_view(), name='survey-detail')
]