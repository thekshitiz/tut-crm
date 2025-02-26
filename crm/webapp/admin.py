from django.contrib import admin
from .models import Client

class ClientAdmin(admin.ModelAdmin):    
    list_display = ('full_name', 'email', 'phone', 'address', 'city', 'state', 'zipcode', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('full_name', 'email', 'phone', 'address', 'city', 'state', 'zipcode')
    ordering = ('-created_at',)

# Register your models here.
admin.site.register(Client, ClientAdmin)

