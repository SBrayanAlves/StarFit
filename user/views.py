from django.shortcuts import render, redirect
from .forms import CreateUser
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

#Def for create new user
def signup(request):
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfully!')
            return redirect('login')
    else:
        form = CreateUser()
    
    return render(request, 'user/signup.html', {'form': form})
    
#Def for login
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email') #pull the email
        password = request.POST.get('password') #pull the password

        #Authenticate the user
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Welcome to the StarFit')
            return redirect('home')
        else:
            messages.error(request, 'Email or password incorrects!')

    return render(request, 'user/login.html')

#Def for logout
def logout_view(request):
    logout(request)
    return redirect('login')