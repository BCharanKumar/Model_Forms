from django.contrib import admin

# Register your models here.
from app.models import *

#Customizeing of the table Based on user requirement
class WebpageCustomize(admin.ModelAdmin):
    list_display=['name','email','url','topic_name']
    list_display_links=['email','name']
    list_editable=['url']
    search_fields=['name']
    list_per_page=2
    list_filter=['name']


class AccessRecordCutomize(admin.ModelAdmin):
    list_display=['date','author','name']
    list_display_links=['date','name']
    list_editable=['author']
    list_filter=['date']
    list_per_page=2
    search_fields=['author']


    
admin.site.register(Topic)
admin.site.register(WebPage,WebpageCustomize)
admin.site.register(AccessRecord,AccessRecordCutomize)