from django.contrib import admin
from .models import AnswerSet



class SurveyAdmin(admin.ModelAdmin):
	pass

admin.site.register(AnswerSet, SurveyAdmin)