from django.urls import path, include
from . import views
urlpatterns = [
    
    path('', views.index, name="index"),
    path('view', views.view, name="view"),
    path('tempo', views.tempo, name="tempo"),
   
]