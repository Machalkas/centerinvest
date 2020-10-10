from django.contrib import admin
from .models import Branch, Services, Queue

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Branch)
admin.site.register(Services)
admin.site.register(Queue)