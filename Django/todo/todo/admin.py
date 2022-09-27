from django.contrib import admin

# Register your models here.
from todo.models import Todo

admin.site.register(Todo)