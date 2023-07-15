from django.contrib import admin
from .models import Question, Choice

""" admin.site.register(Question)
admin.site.register(Choice) """
""" admin.site.site_header = "Pollster Admin" """
admin.site.register([Question, Choice])
