from django.contrib import admin
from .models import Questions, Answers, Surveys

# Register your models here.

admin.site.register(Questions)
admin.site.register(Answers)
admin.site.register(Surveys)