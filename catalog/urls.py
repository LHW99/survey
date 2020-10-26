from django.urls import path
from . import views
from django.urls import include
from django.views.generic import RedirectView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

# home page
urlpatterns = [
  path('', views.index, name='index')
]

# survey display pages
urlpatterns += [
  path('surveys/', views.SurveysListView.as_view(), name='surveys-list'),
  path('surveys/<uuid:pk>/', views.SurveysDetailView.as_view(), name='surveys-detail')
]

# user survey display pages
urlpatterns += [
  path('mysurveys/', views.UserSurveys.as_view(), name='user-surveys'),
]

# for log-ins and authentications
urlpatterns += [
  path('accounts/', include('django.contrib.auth.urls'))
]