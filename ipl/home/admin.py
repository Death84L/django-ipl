from django.contrib import admin

# Register your models here.
from .models import Number_store
from import_export.admin import ImportExportModelAdmin

@admin.register(Number_store)
class userdata(ImportExportModelAdmin):
    pass