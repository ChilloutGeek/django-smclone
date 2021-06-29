from django.urls import path
from . import views 
from .views import HomeFeedView, DetailPostView, DeletePostView, EditPostView

urlpatterns = [
    path('home/', HomeFeedView.as_view(), name='feed'),
    path('edit_post/<str:pk>/', EditPostView.as_view(), name='edit_post'),
    path('delete_post/<str:pk>',DeletePostView.as_view(), name='delete_post'),
    path('detail_post/<str:pk>', DetailPostView.as_view(), name='detail_post'),
    path('like_unlike/<str:pk>', views.postlike, name='like_post'),

]