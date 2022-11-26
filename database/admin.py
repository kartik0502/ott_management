from django.contrib import admin
from .models import Administrator,Employee,User,Subscribers,Feedback,Content,Genre,Language,Rating,Revenue,Show_type,Production_House
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(Administrator,Employee,User,Subscribers,Feedback,Content,Genre,Language,Rating,Revenue,Show_type,Production_House)
class userdat(ImportExportModelAdmin):
    pass