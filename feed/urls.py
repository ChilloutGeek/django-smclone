from django.urls import path
from . import views

urlpatterns = [
    path('home',views.homefeed, name='feed'),
    path('edit_post/<str:pk>/', views.editpost, name='edit_post'),
    path('delete_post/<str:pk>',views.deletepost, name='delete_post')
]