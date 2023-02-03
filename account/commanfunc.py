from django.shortcuts import get_object_or_404
from .models import *
from django.db.models import Q 


"""This function for  view profile check"""
def ViewedProfiles(matrimonyid,requestid,preference):
    """self matrimony id"""
    selfprofile=get_object_or_404(Person,matrimony_id=matrimonyid)
    
    """requested matrimony id"""
    requested_profile=get_object_or_404(Person,matrimony_id=requestid)
    
    view_profile=selfprofile.viewedprofile_set.filter(view=requested_profile,preference=selfprofile.preference)
    
               
    if view_profile.exists():
        return True
    else:
        view_profile=selfprofile.viewedprofile_set \
        .create(view=requested_profile,preference=selfprofile.preference)
        return True
    
    







"""VIEW PHONE NUMBERS"""
"""This function for  view profile check"""
  
def ViewedPhoneNumberStatus(matrimonyid,requestid):
    
    try:
        ViewPhonNumber.objects.get(profile=matrimonyid,view=requestid.id)
        return True
    except Exception as e:
        return False
   

"""check request status"""       
def connect_status(matrimonyid,requestid):
    # assert matrimonyid is None ,"matrimony id can't be None"
    # assert requestid is None ," requested matrimony id can't be None"
    query=Q(
        Q(profile__matrimony_id=matrimonyid,requested_matrimony_id=requestid)
        |
        Q(profile__matrimony_id=requestid,requested_matrimony_id=matrimonyid)
    )
    send_friend_request=FriendRequests.objects.filter(query)
    if send_friend_request.exists():
        return {"connect_status":send_friend_request[0].request_status} 
    else:
        return {"connect_status":"connect"}   


def connect_status_(matrimonyid,requestid):
    # assert matrimonyid is None ,"matrimony id can't be None"
    # assert requestid is None ," requested matrimony id can't be None"
    query=Q(
        Q(profile__matrimony_id=matrimonyid,requested_matrimony_id=requestid)
        |
        Q(profile__matrimony_id=requestid,requested_matrimony_id=matrimonyid)
    )
    send_friend_request=FriendRequests.objects.filter(query)
    if send_friend_request:
        return send_friend_request[0].request_status
    else:
        return "connect"
# def height(string):
#     c=string.split("'")[:2]
#     c_s=c[0]+"."+c[1]
#     return c_s

import datetime

def get_age(string):
    string=string.split("-")
    today=datetime.datetime.today().date()
    dbdate=datetime.date(int(string[0]), int(string[1]),int(string[2]))
    year=today-dbdate
    age= str((year//365))[:3]
    return age.strip()