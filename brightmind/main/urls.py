from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('create-course/', views.create_course, name='create_course'),
    path('create-chapter/', views.create_chapter, name='create_chapter'),
]
