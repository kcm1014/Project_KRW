from django.urls import path
from . import  views

urlpatterns = [
    path('write/',views.write,name='write'),
    path('write_data/',views.writeData,name='writeData'),
    path('get_subcategory/',views.getSubcategory,name='getSubcategory'),
]