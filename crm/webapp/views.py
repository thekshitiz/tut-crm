from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    # check the logged in user
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in')
            return redirect('home')
        else:
            messages.success(request, 'There was an error logging in, please try again')
            return redirect('home')
    return render(request, 'home.html', {})

# this function we will use to create a separate login page
# def login_view(request):
#     return render(request, 'login.html', {})

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')
    pass


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'Registration successful and you are now logged in')
            return redirect('home')
    else:
        form = UserCreationForm()    

    return render(request, 'register.html', {'form': form})