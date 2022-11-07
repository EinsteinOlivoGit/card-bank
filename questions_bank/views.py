from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')


    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('pass')
    
        user = authenticate(request, username=username, password=password)

        if user is not None:
            print(user)
            login(request=request, user=user)
            return redirect('/')
        else:
            messages.info(request, 'Username or Password is incorrect')
        
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('login')
