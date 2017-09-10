from django.contrib import admin

from .models import Users, Idea, Feedback
# Register your models here.
admin.site.register(Users)
admin.site.register(Idea)
admin.site.register(Feedback)

