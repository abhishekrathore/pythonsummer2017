from django.contrib import admin

# Register your models here.
from .models import Person,ClassRoom

admin.site.register(Person)
admin.site.register(ClassRoom)

