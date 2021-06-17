from django.shortcuts import render,redirect

from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm
from .models import Profile

def login_acc(request):
    
    form = LoginForm()

    if request.method == "POST":
        
        form = LoginForm(request.POST, request=request)
        
        if form.is_valid():
            
            login(request, form.user)
            
            return redirect("feed")

    return render(request, 'accounts/loginpage.html', {'form':form})

# Create your views here.

def logout_acc(request):

    logout(request)

    return redirect('login')

def follow_unfollow_profile(request,pk):
    
    profile = Profile.objects.get(id=pk)
    my_profile = Profile.objects.get(user=request.user)

    my_profile_following = my_profile.following.filter(id=profile.user.id)
    is_following = profile.following.filter(id=request.user.id)

    
    if my_profile_following.exists():

        my_profile.following.remove(profile.user)
    
    else:

        my_profile.following.add(profile.user)


    return redirect('profile_detail',pk=pk)
def profile_detail(request,pk):

    profile = Profile.objects.get(pk=pk)

    my_profile = Profile.objects.get(user=request.user)

    my_profile_following = my_profile.following.filter(id=profile.user.id)

    is_following = profile.following.filter(id=request.user.id)
    
    return render(request, 'accounts/profiledetail.html',{'profile':profile,'is_following':is_following,'my_profile':my_profile,'my_profile_following':my_profile_following})
