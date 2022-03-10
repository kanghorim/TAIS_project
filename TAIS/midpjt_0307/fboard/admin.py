from django.contrib import admin

from fboard.models import News_Info, Notice, Related_Info


# Register your models here.
admin.site.register(Related_Info)

admin.site.register(News_Info)

admin.site.register(Notice)