from django.db import models
from django.urls import reverse # Used to generate URLs by reversing URL patterns
import uuid # required for unique instances
from django.contrib.auth.models import User # lets us use user
from datetime import date

# Create your models here.
class Answer(models.Model):
  ans = models.CharField(max_length=200)

  def __str__(self):
    return self.name

class Questions(models.Model):
  ques = models.CharField(max_length=300)

  def __str__(self):
    return self.name

class Survey(models.Model):
  def __str__(self):
    return self.name