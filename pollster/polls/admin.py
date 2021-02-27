from django.contrib import admin

from polls.models import Choice, Question

admin.site.site_header = "Pollster Admin"
admin.site.index_title = "Pollster Admin"
admin.site.site_title = "Pollster Admin"

admin.site.register(Question)
admin.site.register(Choice)
