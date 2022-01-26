from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('resource/', views.resource, name='resource'),
    #path('blog/', views.blog, name='blog'), 
    path('findtutors/', views.findtutors, name='findtutors')
]