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

def profile_detail(request,pk):

    profile = Profile.objects.get(pk=pk)

    my_profile = Profile.objects.get(user=request.user)
    
    if profile.user in my_profile.following.all():
        follow = True
    else:
        follow = False


    return render(request, 'accounts/profiledetail.html',{'profile':profile,'follow':follow})
