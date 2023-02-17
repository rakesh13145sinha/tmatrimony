from rest_framework.response import Response 
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from account.models import *
from django.db.models import Count,Q


from adminuser.serializers import AdminPersonSerializer
from connect.models import DocumentUpload

# Create your views here.
@api_view(['GET'])
def dashboard(request):
    dashboard=Person.objects.\
    aggregate(male=Count("gender",filter=Q(gender="Male")),
             female=Count("gender",filter=Q(gender="Female")),
             subscribe=Count("active_plan",filter=Q(active_plan='Trial')))
    return Response(dashboard)


@api_view(['GET'])
def gender(request):
    profiles=Person.objects.filter(gender=request.GET['gender']).only('id').order_by('-id')
    response={}
    for pro in profiles:
        images=pro.profilemultiimage_set.filter(files__isnull=False)
        response[pro.id]={
            "id":pro.id,
            "matrimony_id":pro.matrimony_id,
            "image":images[0].files.url if images.exists() else None,
            "gender":pro.gender,
            "name":pro.name,
            "phone_number":pro.phone_number,
            "status":pro.status
            
        }
        
        
    return Response(response.values(),status=200)


@api_view(['GET'])
def profile(request):
    profile=Person.objects.get(id=request.GET['id'])
    images=profile.profilemultiimage_set.all()
    serializers=AdminPersonSerializer(profile,many=False).data
    serializers['image']=images[0].files.url if images.exists() else None
    return Response(serializers,status=200)
    

@api_view(['GET'])
def search(request):
    profile=Person.objects.values(request.GET['q']).distinct()
    return Response(profile,status=200)

@api_view(['GET'])
def document_upload_view(request):
    
    response={}
    who_upload_docs=DocumentUpload.objects.values_list('profile__id',flat=True).distinct()
    profiles=Person.objects.filter(id__in=who_upload_docs)
    
    for profile in profiles:
        doc=profile.documentupload_set.values("name_of_document","status","created_date")
            
        response[profile.id]={
            "matrimony_id":profile.matrimony_id,
            "name":profile.name,
            "docs":doc
        }
        
    return Response(response.values())

        



    


    
    