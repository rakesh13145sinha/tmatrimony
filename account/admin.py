from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(City)
# admin.site.register(State)
admin.site.register(SaveOTP)
admin.site.register(BannerImage)
admin.site.register(HomeScreenImage)
class PersonAdmin(admin.ModelAdmin):
    #list_display=['matrimony_id','name','religion','phone_number',"marital_status",'caste','gender','dosham']
    list_display=['matrimony_id','name',"marital_status",'gender']
    list_editable=['marital_status']
    list_filter=['gender',"marital_status"]
class FriendRequestsAdmin(admin.ModelAdmin):
    list_display=['requested_matrimony_id','request_status','preference']
   
    list_editable=['preference']
    
class MatchOfDayAdmin(admin.ModelAdmin):
    list_display=['profile','view','preference','add_date']
    list_editable=['preference']
    list_filter=['profile']

admin.site.register(Person,PersonAdmin)
admin.site.register(ViewedProfile)
admin.site.register(MatchOfDay,MatchOfDayAdmin)
admin.site.register(FriendRequests,FriendRequestsAdmin)