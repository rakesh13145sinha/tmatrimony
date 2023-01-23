from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(City)
# admin.site.register(State)
admin.site.register(SaveOTP)
admin.site.register(BannerImage)
admin.site.register(HomeScreenImage)
class PersonAdmin(admin.ModelAdmin):
    list_display=['matrimony_id','name','religion','phone_number',"region",'preference']
    list_editable=['region']
    list_filter=['preference','active_plan','religion']
admin.site.register(Person,PersonAdmin)
admin.site.register(ProfileMultiImage)