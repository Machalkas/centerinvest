from django.contrib import admin
from .models import test

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(test, AuthorAdmin)