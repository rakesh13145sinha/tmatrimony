from functools import reduce
from rest_framework.decorators import api_view
from rest_framework.response import Response
from account.models import FriendRequests, Person
from account.serializers import TabPersonSerializer
from django.db.models import Q



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





"""SEARCH BY MATRIMONY ID"""
@api_view(['GET'])
def search_by_matrimonyid(request):
    logged_matrimony_id=request.GET['matrimony_id']
    search_matrimony_id=request.GET['requeted_matrimony_id']
    try:
        logged_user=Person.objects.get(matrimony_id=logged_matrimony_id)
    except Exception as e:
        return Response({"message":"Invalid matrimony id"},status=200)
    try:
        search_mid=Person.objects.get(matrimony_id__iexact=search_matrimony_id)
    except Exception as e:
        return Response({"message":"Invalid requested matrimony id"},status=200)
    if logged_user.gender!=search_mid.gender:
        serializer=TabPersonSerializer(search_mid, context={'matrimony_id':logged_matrimony_id},many=False)                         
        return Response(serializer.data)
    else:
        return Response({"matrimony_id":None},status=200)
    
    
    
"""SEARCH BY ANY THING"""   
@api_view(['POST'])
def search_test(request):
    
    logged_matrimony_id=request.GET['matrimony_id']
    
    
    #data = ast.literal_eval(request.data['nameValuePairs'])
    data = request.data['nameValuePairs']
   
    #data=request.data 
    print(">>>>>>>>>>>>>>>")
    print(data)
    print(">>>>>>>>>>>>>>>")
    try:
        profile=Person.objects.get(matrimony_id=logged_matrimony_id)
    except Exception as e:
        return Response({"message":"Invalid matrimony id"},status=400)
    
    
    _height_list=[
    "3'1''","3'2''","3'3''","3'4''","3'5''","3'6''","3'7''","3'8''","3'9''","3'10''","3'11''","4'0''" , 
    "4'1''","4'2''","4'3''","4'4''","4'5''","4'6''","4'7''","4'8''","4'9''","4'10''","4'11''","5'0''" , 
    "5'1''","5'2''","5'3''","5'4''","5'5''","5'6''","5'7''","5'8''","5'9''","5'10''","5'11''","6'0''",
    "6'1''","6'2''","6'3''","6'4''","6'5''","6'6''","6'7''","6'8''","6'9''","6'10''","6'11''","7'0''",
    "7'1''","7'2''","7'3''","7'4''","7'5''","7'6''","7'7''","7'8''","7'9''","7'10''","7'11''","8'0''"
        
        ]
    
    _index={"min_height":_height_list.index(data['min_height']),
            "max_height":_height_list.index(data['max_height'])
            }
    
    #base filter query
    query=~Q(gender=profile.gender,status=False )
    #gender=~Q(gender=profile.gender,status=False )
    

    
    
   
   
    # q_list=[]
    # h_and_age=Q(
    #     height__in=[i for i in _height_list[ _index['min_height']:_index['max_height'] ] ],
    #          dateofbirth__range=(data['min_age'],data['max_age'] )
    # )
    query=~Q(gender=profile.gender,status=False)  & Q(
                height__in=[i for i in _height_list[ _index['min_height']:_index['max_height'] ] ],
                dateofbirth__range=(data['min_age'],data['max_age'] )
                )
                
               
                
                
               
            
    # q_list.append(gender)
    # q_list.append(h_and_age)
    
    if data['country']!="Any":
        country=Q(country__in=data['country'].split(","),)
        #query=query & country 
        query=query.add(country,Q.AND)
        #q_list.append(country)
    if data['state']!="Any":
        state=Q(state__in=data['state'].split(","))
        #q_list.append(state)
        #query=query & state
        query=query.add(state,Q.AND)
    if data['city']!="Any":
        city=Q(city__in=data['city'].split(","))
        #q_list.append(city)
        #query=query & city
        query=query.add(city,Q.AND)
        
        
        
    #for any field
   
    
    
    #matrital status
    if data['marital_status']!="Any":
        marital_status=Q(marital_status__in=data['marital_status'].split(","))
        query=query & marital_status  #(country,Q.AND)
    if data['mother_tongue']!="Any":
        mother_tongue=Q(mother_tongue__in=data['mother_tongue'].split(","))
        query=query & mother_tongue
    if data['physical_status']!="Any":
        physical_status=Q(physical_status__in=data['physical_status'].split(","))
        query=query & physical_status
       
    # #profession base filter
    
    if data['occupation']!="Any":
        occupation=Q(occupation__in=data['occupation'].split(","))
        query=query & occupation
    if data['qualification']!="Any":
        qualification=Q(qualification__in=data['qualification'].split(","))
        query=query & qualification
    
    if data['min_income']!="Any":
        annual_income=Q(annual_income__startswith=data['min_income'])
        #query.add(annual_income,Q.AND)
        query=query & annual_income
        
    if data['max_income']!="Any":
        annual_income=Q(annual_income__startswith=data['max_income'])
        #query.add(annual_income,Q.AND)
        query=query & annual_income
    
    #religious base filter
    
    if data['religion']!="Any":
        religion=Q(religion__in=data['religion'].split(","))
        query=query & religion
    if data['caste']!="Any":
        caste=Q(caste__in=data['caste'].split(","))
        query=query & caste
    if data['dosham']!="Any":
        dosham=Q(dosham__in=data['dosham'].split(","))
        query=query & dosham
    if data['star']!="Any":
        star=Q(star__in=data['star'].split(","))
        query=query & star
    
    
    
    # #profession base filter
    
    if data['occupation']=="Any":
        occupation=Q(occupation__isnull=False)& ~Q(gender=profile.gender)
        query=query & occupation
        #query.add(occupation,Q.AND)
    if data['qualification']=="Any":
        qualification=Q(qualification__isnull=False)& ~Q(gender=profile.gender)
        query=query & qualification
    if data['min_income']=="Any":
        annual_income=Q(annual_income__isnull=False)& ~Q(gender=profile.gender)
        query=query & annual_income
    
    #religious base filter
    
    if data['religion']=="Any":
        religion=Q(occupation__isnull=False)& ~Q(gender=profile.gender)
        query=query & religion
    if data['caste']=="Any":
        caste=Q(caste__isnull=False)& ~Q(gender=profile.gender)
        query=query & caste
    if data['dosham']=="Any":
        dosham=Q(dosham__isnull=False)& ~Q(gender=profile.gender)
        query=query & dosham
    if data['star']=="Any":
        star=Q(star__isnull=False)& ~Q(gender=profile.gender)
        query=query & star#(star,Q.AND)
  
    if data['marital_status']=="Any":
        marital_status=Q(marital_status__isnull=False)& ~Q(gender=profile.gender)
        query=query & marital_status
    if data['mother_tongue']=="Any":
        mother_tongue=Q(mother_tongue__isnull=False)& ~Q(gender=profile.gender)
        query=query & mother_tongue
    if data['physical_status']=="Any":
        physical_status=Q(physical_status__isnull=False) & ~Q(gender=profile.gender)
        query=query & physical_status

    if data['country']=="Any":
        country=Q(country__isnull=False)& ~Q(gender=profile.gender)
        query=query & country
    if data['state']=="Any":
        state=Q(state__isnull=False)& ~Q(gender=profile.gender)
        query=query & state
    if data['city']=="Any":
        city=Q(city__isnull=False)& ~Q(gender=profile.gender)
        query=query & city
    
    
    
    
     
    response={}
    
    #print(query)
   
    # r_profile=Person.objects.filter(reduce(operator.and_, q_list))
    r_profile=Person.objects.filter(query).only('id').order_by('-reg_date')
    #print(r_profile)
    for r_pro in r_profile:
       
        response[r_pro.id]={
            "matrimony_id":r_pro.matrimony_id,
            "profileimage":[{"image":r_pro.profilemultiimage_set.latest('id').files.url if r_pro.profilemultiimage_set.all() else None}],
            "height":r_pro.height,
            "dateofbirth":r_pro.dateofbirth,
            "gender":r_pro.gender,
            "name":r_pro.name,
            "phone_number":r_pro.phone_number,
            "occupation" :r_pro.occupation,
            "city":r_pro.city,
            "state":r_pro.state,
            "qualification":r_pro.qualification ,
            "active_plan":r_pro.active_plan
            
        }
        response[r_pro.id].update(connect_status(logged_matrimony_id,r_pro.matrimony_id))
    
    
    return Response(response.values(),status=200)    
    
    

    



"""SEARCH BY ANY THING"""   
@api_view(['GET'])
def search_test1(request):
    logged_matrimony_id=request.GET['matrimony_id']
    data=request.data 
    # try:
    #     profile=Person.objects.get(matrimony_id=logged_matrimony_id)
    # except Exception as e:
    #     return Response({"message":"Invalid matrimony id"},status=400)
    
    _height_list=[
    "3'1''","3'2''","3'3''","3'4''","3'5''","3'6''","3'7''","3'8''","3'9''","3'10''","3'11''","4'0''" , 
    "4'1''","4'2''","4'3''","4'4''","4'5''","4'6''","4'7''","4'8''","4'9''","4'10''","4'11''","5'0''" , 
    "5'1''","5'2''","5'3''","5'4''","5'5''","5'6''","5'7''","5'8''","5'9''","5'10''","5'11''","6'0''",
    "6'1''","6'2''","6'3''","6'4''","6'5''","6'6''","6'7''","6'8''","6'9''","6'10''","6'11''","7'0''",
    "7'1''","7'2''","7'3''","7'4''","7'5''","7'6''","7'7''","7'8''","7'9''","7'10''","7'11''","8'0''"
        
        ]
    
    _index={"min_height":_height_list.index(data['min_height']),
            "max_height":_height_list.index(data['max_height'])
            }
    
    #base filter query
    #query=~Q(gender=profile.gender,status=False) 
    query=~Q(gender="Male",status=False)
             
             
             
    #height and age
    h_and_age=Q(
        height__in=[i for i in _height_list[ _index['min_height']:_index['max_height'] ] ],
             dateofbirth__range=(data['min_age'],data['max_age'] )
    )
    query=query & h_and_age
    
    if data['country']!="Any":
        country=Q(country__in=data['country'].split(","),)
        query=query | country  #(country,Q.AND)
    if data['state']!="Any":
        state=Q(state__in=data['state'].split(","))
        #query.add(state,Q.AND)
        query=query | state
    if data['city']!="Any":
        city=Q(city__in=data['city'].split(","))
        #query.add(city,Q.AND)
        query=query | city
        
        
        
    #for any field
    if data['country']=="Any":
        country=Q(country__isnull=False)
        query.add(country,Q.OR)
    if data['state']=="Any":
        state=Q(state__isnull=False)
        query.add(state,Q.OR)
    if data['city']=="Any":
        city=Q(city__isnull=False)
        query.add(city,Q.OR)
    
    
    #matrital status
    if data['marital_status']!="Any":
        marital_status=Q(marital_status__in=data['marital_status'].split(","))
        query=query | marital_status  #(country,Q.AND)
    if data['mother_tongue']!="Any":
        mother_tongue=Q(mother_tongue__in=data['mother_tongue'].split(","))
        query=query | mother_tongue
    if data['physical_status']!="Any":
        physical_status=Q(physical_status__in=data['physical_status'].split(","))
        query=query | physical_status
        
        
        
    #for any field
    if data['marital_status']=="Any":
        marital_status=Q(marital_status__isnull=False)
        query.add(marital_status,Q.OR)
    if data['mother_tongue']=="Any":
        mother_tongue=Q(mother_tongue__isnull=False)
        query.add(mother_tongue,Q.OR)
    if data['physical_status']=="Any":
        physical_status=Q(physical_status__isnull=False)
        query.add(physical_status,Q.OR)
    
    
    
    
    # #profession base filter
    
    if data['occupation']!="Any":
        occupation=Q(occupation__in=data['occupation'].split(","))
        #query.add(occupation,Q.AND)
        query=query | occupation
    if data['qualification']!="Any":
        qualification=Q(qualification__in=data['qualification'].split(","))
        #query.add(qualification,Q.AND)
        query=query | qualification
    # if data['job_sector']!="Any":
    #     job_sector=Q(job_sector__in=data['job_sector'].split(","))
    #     query.add(job_sector,Q.OR)
    if data['annual_income']!="Any":
        annual_income=Q(annual_income__in=data['annual_income'].split(","))
        #query.add(annual_income,Q.AND)
        query=query | annual_income
    
    # #religious base filter
    
    if data['religion']!="Any":
        religion=Q(religion__in=data['religion'].split(","))
        query.add(religion,Q.OR)
    if data['caste']!="Any":
        caste=Q(caste__in=data['caste'].split(","))
        query.add(caste,Q.OR)
    if data['dosham']!="Any":
        dosham=Q(dosham__in=data['dosham'].split(","))
        query.add(dosham,Q.OR)
    if data['star']!="Any":
        star=Q(star__in=data['star'].split(","))
        query.add(star,Q.OR)
    
    
    # ##if any field search for any###################
    
    #  #location query
    
    
   
    # #profession base filter
    
    if data['occupation']=="Any":
        occupation=Q(occupation__isnull=False)
        query.add(occupation,Q.OR)
    if data['qualification']=="Any":
        qualification=Q(qualification__isnull=False)
        query.add(qualification,Q.OR)
    # if data['job_sector']=="Any":
    #     job_sector=Q(job_sector__isnull=False)
    #     query.add(job_sector,Q.OR)
    if data['annual_income']=="Any":
        annual_income=Q(annual_income__isnull=False)
        query.add(annual_income,Q.OR)
    
    # #religious base filter
    
    if data['religion']=="Any":
        religion=Q(occupation__isnull=False)
        query.add(religion,Q.OR)
    if data['caste']=="Any":
        caste=Q(caste__isnull=False)
        query.add(caste,Q.OR)
    if data['dosham']=="Any":
        dosham=Q(dosham__isnull=False)
        query.add(dosham,Q.OR)
    if data['star']=="Any":
        star=Q(star__null=False)
        query=query(star,Q.OR)
  
        
    
    
    
    print(query)   
    response={}
    r_profile=Person.objects.filter(query).only('id').order_by('-reg_date')
    print()
    print()
    print("================================================")
    print(r_profile.query)
    print("================================================")
    for r_pro in r_profile:
       
        response[r_pro.id]={
            "matrimony_id":r_pro.matrimony_id,
            "image":r_pro.profilemultiimage_set.latest('id').files.url if r_pro.profilemultiimage_set.all() else None,
            "height":r_pro.height,
            "age":r_pro.dateofbirth,
            "gender":r_pro.gender,
            "name":r_pro.name,
            "phone_number":r_pro.phone_number
            
        }
        response[r_pro.id].update(connect_status(logged_matrimony_id,r_pro.matrimony_id))
    
    return Response(response.values(),status=200)


   
    
    

    
    
    
    
    
    


    
    
    
    
    
   