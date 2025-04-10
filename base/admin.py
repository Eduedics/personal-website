from django.contrib import admin
from .models import Projects,Tag ,description

# Register your models here.

admin.site.register(Projects)
admin.site.register(Tag)
admin.site.register(description)
