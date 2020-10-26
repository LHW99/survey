from django.contrib import admin
from .models import Questions, Answers, Surveys

# Register your models here.

class AnswersInline(admin.TabularInline):
  model = Answers

class QuestionsAdmin(admin.ModelAdmin):
  inlines = [
    AnswersInline,
  ]

class QuestionsInline(admin.TabularInline):
  model = Questions

class SurveysAdmin(admin.ModelAdmin):
  inlines = [
    QuestionsInline,
  ]

admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Answers)
admin.site.register(Surveys, SurveysAdmin)