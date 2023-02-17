from django.urls import path
from . import  views
app_name = 'rate'
urlpatterns = [
    path('list/', views.list, name='list'),
    path('detail/<int:ratecontent_id>/',views.detail,name='detail'),
    path('delete/<int:ratecontent_id>/',views.delete,name='delete'),
    path('showResult/<int:ratecontent_id>/<int:result_code>/', views.showResult, name='showResult'),
    path('write/',views.write,name='write'),
    path('write_data/',views.writeData,name='writeData'),
    path('get_subcategory/',views.getSubcategory,name='getSubcategory'),
]