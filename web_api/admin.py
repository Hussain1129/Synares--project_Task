from django.contrib import admin
from .models import StudentModel, WebUrl, Urldetail


# Register your models here.

admin.site.register(StudentModel)
admin.site.register(WebUrl)
admin.site.register(Urldetail)
