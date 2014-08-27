from django.contrib import admin
from .models import AnswerSet, School

class SurveyAdmin(admin.ModelAdmin):
	pass

admin.site.register(School)
admin.site.register(AnswerSet, SurveyAdmin)