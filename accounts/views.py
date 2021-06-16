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

    is_following = profile.following.filter(id=request.user.id)

    if is_following.exists():
        profile.following.remove(request.user)
    else:
        profile.following.add(request.user)


    return redirect('profile_detail',pk=pk)
def profile_detail(request,pk):

    profile = Profile.objects.get(pk=pk)

    is_following = profile.following.filter(id=request.user.id)
    
    


    return render(request, 'accounts/profiledetail.html',{'profile':profile,'is_following':is_following})
