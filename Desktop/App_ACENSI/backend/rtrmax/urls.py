from django.urls import path,include
from . import views 

app_name="rtrmax"

urlpatterns = [
    path('', views.index, name='index' ),
    path('new_index/', views.nindex, name='new_index' )
    
]