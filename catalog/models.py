from django.db import models
from django.urls import reverse # Used to generate URLs by reversing URL patterns
import uuid # required for unique instances
from django.contrib.auth.models import User # lets us use user
from datetime import date

# Create your models here.
class Answers(models.Model):
  answer = models.CharField(max_length=200)
  question = models.ForeignKey('Questions', on_delete=models.SET_NULL, null=True)

  def __str__(self):
    return self.answer

class Questions(models.Model):
  question = models.CharField(max_length=300)
  survey = models.ForeignKey('Surveys', on_delete=models.SET_NULL, null=True)

  def __str__(self):
    return self.question

class Surveys(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4)
  name = models.CharField(max_length=300)
  survey_taker = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

  class Meta:
    permissions = (('can_edit_survey', 'Edit Survey'),)

  def get_absolute_url(self):
    return reverse('surveys-detail', args=[str(self.id)])

  def __str__(self):
    return self.name