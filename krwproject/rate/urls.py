from django.urls import path
from . import  views
app_name = 'rate'
urlpatterns = [
    path('list/', views.list, name='list'),
    path('detail/', views.detail, name='detail'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('showResult/<int:page>/<int:categoryId>/<int:subcategoryId>/<int:ratecontent_id>/<str:sort>/<int:result_code>/', views.showResult ,name='showResult'),
    path('write/', views.write, name='write'),
    path('write_data/', views.writeData, name='writeData'),
    path('get_subcategory/', views.getSubcategory, name='getSubcategory'),

]