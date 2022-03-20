from django.contrib import admin

from schoole_system.api.models import Question, Choice, Assignment

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Assignment)
