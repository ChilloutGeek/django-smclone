from django.urls import path
from .views import login_acc, logout_acc, profile_detail, follow_unfollow_profile

urlpatterns = [
    path('login/', login_acc, name='login'),
    path('logout_acc', logout_acc, name='logout'),
    path('profile/<pk>/',profile_detail, name='profile_detail' ),
    path('switchfollow/<pk>/', follow_unfollow_profile, name='follow_unfollow')
]