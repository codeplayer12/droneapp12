from django.contrib import admin
from .models import Category, Photo,Upload,Report
# Register your models here.

admin.site.register(Report)

class ReportInline(admin.StackedInline):
    model  = Report

class UploadAdmin(admin.ModelAdmin):
    inlines = [ReportInline,]
admin.site.register(Upload,UploadAdmin)