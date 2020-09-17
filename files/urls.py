from django.urls import path
from .views import *

app_name = 'files'

urlpatterns = [
    # File 
    path('v1/file', Files_APIView.as_view()), 
    path('v1/file/<int:pk>', Files_APIView_Detail.as_view()),
    
]