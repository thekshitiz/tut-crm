from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.db.models import Q
from .models import Client, Order
from .forms import AddClientForm, OrderForm

# Create your views here.
def home_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('home')
    
    return render(request, 'home.html')

# this function we will use to create a separate login page
# def login_view(request):
#     return render(request, 'login.html', {})

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')
    pass


def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful')
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def dashboard_view(request):
    clients = Client.objects.all().order_by('-created_at')
    return render(request, 'dashboard.html', {'clients': clients})

@login_required
def client_view(request, pk):
    client = get_object_or_404(Client, pk=pk)
    orders = client.orders.all().order_by('-order_date')
    return render(request, 'client.html', {'client': client, 'orders': orders})

@login_required
def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    client.delete()
    messages.success(request, 'Client deleted successfully')
    return redirect('dashboard')
    

@login_required
def add_client(request):
    if request.method == 'POST':
        form = AddClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client added successfully')
            return redirect('dashboard')
    else:
        form = AddClientForm()
    return render(request, 'add_client.html', {'form': form})

@login_required
def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = AddClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client updated successfully')
            return redirect('dashboard')
    else:
        form = AddClientForm(instance=client)
    return render(request, 'client_update.html', {'form': form})

class HomeView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'dashboard.html'
    context_object_name = 'clients'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Client.objects.all()
        search_query = self.request.GET.get('search', '')
        
        if search_query:
            queryset = queryset.filter(
                Q(full_name__icontains=search_query) |
                Q(email__icontains=search_query) |
                Q(phone__icontains=search_query) |
                Q(city__icontains=search_query) |
                Q(state__icontains=search_query)
            )
        
        return queryset.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        return context

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    
    return redirect('home')
