from django.contrib import admin
from django.urls import path
from fireapp import views
urlpatterns = [
    path('admin/', admin.site.urls),  
    path('', views.index, name='index'),
    path('insert/',views.insert,name='insert'),
    path('data/',views.data,name='data'),
    path('delete/<id>/',views.delete,name='delete'),
    path('edit/<id>/',views.edit,name='edit'),
    path('update/',views.update,name='update'),
 
]