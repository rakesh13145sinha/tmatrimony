from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(City)
# admin.site.register(State)
admin.site.register(SaveOTP)
admin.site.register(BannerImage)
admin.site.register(HomeScreenImage)
class PersonAdmin(admin.ModelAdmin):
    list_display=['matrimony_id','name','religion','phone_number',"region",'caste']
    list_editable=['region','caste']
    list_filter=['caste','religion']
class FriendRequestsAdmin(admin.ModelAdmin):
    list_display=['requested_matrimony_id','request_status','preference']
   
    list_editable=['preference']
admin.site.register(Person,PersonAdmin)
admin.site.register(ProfileMultiImage)
admin.site.register(FriendRequests,FriendRequestsAdmin)