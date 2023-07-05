from django.contrib import admin
from .models import StudentModel, WebUrl, Urldetail


# Register your models here.

admin.site.register(StudentModel)
admin.site.register(WebUrl)


@admin.register(Urldetail)
class Urldetailadmin(admin.ModelAdmin):
    list_display = ["id", "weburls", "counts", "userurl", "updated"]
