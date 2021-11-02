from django.urls import path
from . import views


app_name = 'app'
urlpatterns = [
    path('', views.View, name = 'View'),
    path('get/', views.GetFile, name = 'Get File'),
    path('add/', views.AddFile, name='Add File'),
    path('del/', views.Delete, name = 'Delete File')
]