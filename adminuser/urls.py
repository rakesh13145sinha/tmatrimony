from django.urls import path
from .views import *
urlpatterns = [
    path('dashboard',dashboard),
    path('gender',gender),
    path('profile',profile),
    path('search',search),
    path('document',document_upload_view,name="upload document")
]
