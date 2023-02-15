from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Person,Partner_Preferences,SaveOTP

from account.commanfunc import get_age





def create_partner_preferance(pk):
    pp=Person.objects.get(id=pk)
    _,created=Partner_Preferences.objects.get_or_create(profile= pp,min_age= "18",  \
                 max_age="40",min_height="4ft", max_height="7ft",  \
                 physical_status="Doesn't matter", mother_tongue="Any",  \
                 marital_status="Doesn't matter", drinking_habbit="Any",  \
                 smoking_habbit="Any",food="Any",  \
                 caste="Any", religion="Any",star="Any",occupation="Any",  \
                 annual_income= "Any",job_sector="Any",qualification="Any",  \
                 city="Any",state="Any",country= "India",dosham="Any" ,\
                description="Good luck !"
                 
                )
    return created


def generate_matrimonyid():

    clients=Person.objects.order_by('-id')[0:2]
    
    if clients.count() >= 2:
        return  "DM"+str(int(clients[1].matrimony_id[2:])+1)
    else:
        return "DM"+str(102023+1)
    
    

@receiver(post_save, sender=Person)
def create_profile(sender, instance, created, **kwargs):
    if created:
        instance.matrimony_id=generate_matrimonyid()
        instance.dateofbirth=get_age(instance.dateofbirth)
        
        instance.save()
        print(instance.dateofbirth)
        # sending_otp(random.randint(1000,9999), instance.phone_number)
        SaveOTP.objects.update_or_create(phone_number=instance.phone_number,otp=1234)
        create_partner_preferance(instance.id)
        



