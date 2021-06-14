from django.shortcuts import render,redirect

from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm


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