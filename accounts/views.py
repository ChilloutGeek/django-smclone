from django.shortcuts import render,redirect

from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm, SignUpForm
from .models import Profile
from feed.models import Post

def signup_acc(request):
    
    form = SignUpForm()

    if request.method == 'POST':
        
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            return redirect('login')
    else:
        form = SignUpForm()
    
    return render(request, 'accounts/signup.html', {'form': form})

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
    
    import pdb 
    pdb.set_trace()
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
    

    posts = Post.objects.filter(author=profile.user)

    return render(request, 'accounts/profiledetail.html',{'profile':profile,'is_following':is_following,'my_profile':my_profile,'my_profile_following':my_profile_following,'posts':posts})
