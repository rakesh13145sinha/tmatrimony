# states=["Andhra Pradesh","Telangana","Odisa",'Bihar','Madhay Pradesh','Manipur','Assam','West Bangal',
#        'Jharkhand','Gujrat','Maharashtra','Kerala','Tamil Nadu','Sikim','Jammu & Kashmir','Delhi','Rajsthan',
#        'Goa','Nagaland','Uttar Padesh','Panjab','Himacha Pradesh','Chhatishgarh']






# telangana=["Hyderabad","Ranga Reddy","Nizamabad","Khammam","Karimnagar","Adilabad",
#         "Mahbubnagar","Medak","Nalgonda","Warangal","Ramagundam","Suryapet","Miryalaguda","Jagtial"]
# andhara=['Visakhapatnam', 'Vijayawada', 'Krishna', 'Guntur', 'Nellore', 'Kurnool', 'Kadapa', 'Rajahmundry', 'East Godavari', 
#         'Kakinada', 'Tirupati', 'Chittor', 'Eluru', 'West GodavariVisakhapatnam']

# Religion=["Hindu", "Muslim", "Christian", "Sikh", "Jain", "Parsi", "Buddhist"]


# from account.models import Country,State,City
# try:
#     india=Country.objects.get(name="India")
# except Exception as e:
#     india=Country.objects.create(name="India")
# for state in states:
#     get,create=State.objects.get_or_create(name=state,country=india)
#     if get.name=="Telangana":
#         for town in telangana:
            
#             City.objects.get_or_create(name=town,state=get)
#     elif get.name=="Andhra Pradesh":
#         for town in andhara:
#             City.objects.get_or_create(name=town,state=get)
#     else:
#         pass

# from selenium import webdriver
# from bs4 import BeautifulSoup
# import pandas as pd
# import requests
# web=requests.get('https://www.britannica.com/topic/list-of-cities-and-towns-in-India-2033033')
# content=web.text
# soup = BeautifulSoup(content)
# #print(soup.prettify())
# state_list=[]
# for a in soup.findAll('h2', attrs={'class':'h1'}):
        
#         print(a)
#         title_element = a.find("a", class_="md-crosslink")
#         print(title_element.text)
#         state_list.append(title_element.text)
# print(state_list)


    
        

        