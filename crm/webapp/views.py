from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import Client
from .forms import AddClientForm

# Create your views here.
def home(request):
    # grab all the client data records
    clients = Client.objects.all()
    
    # check if it's a POST request (login attempt)
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
    
    # if it's a GET request, just render the page
    return render(request, 'home.html', {'clients': clients })

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

def client(request, pk):
    if request.user.is_authenticated:
        # look up the specific client date
        client_record = Client.objects.get(id=pk)
        return render(request, 'client.html', {'client': client_record})
    else:
        messages.success(request, 'You must be logged in to view this page')
        return redirect('home')

def client_delete(request, pk):
    if request.user.is_authenticated:
        delete_record = Client.objects.get(id=pk)
        delete_record.delete()
        messages.success(request, 'Client record deleted successfully')
        return redirect('home')
    else:
        messages.success(request, 'You must be logged in to delete a client record')
        return redirect('home')
    

def add_client(request):
    form = AddClientForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'Client added successfully')
                return redirect('home')
            else:   
                messages.error(request, 'There was an error adding the client')
        return render(request, 'add_client.html', {'form': form})
    else:
        messages.success(request, 'You must be logged in to add a client')
        return redirect('home')

def client_update(request, pk):
    if request.user.is_authenticated:
        current_record = Client.objects.get(id=pk)
        form = AddClientForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client updated successfully')
            return redirect('home')
        return render(request, 'client_update.html', {'form': form})
    else:
        messages.success(request, 'You must be logged in to update a client')
        return redirect('home') 
