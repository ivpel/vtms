from django.contrib import admin
from .models import Suite, Case, Project

# Register your models here.
admin.site.register(Project)
admin.site.register(Suite)
admin.site.register(Case)
