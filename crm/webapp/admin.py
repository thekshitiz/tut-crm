from django.contrib import admin
from django.http import HttpResponse
import csv
from .models import Client, Order

class OrderInline(admin.TabularInline):
    model = Order
    extra = 0

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):    
    list_display = ('full_name', 'email', 'phone', 'city', 'total_orders', 'total_spent', 'created_at')
    list_filter = ('created_at', 'city', 'state')
    search_fields = ('full_name', 'email', 'phone', 'address', 'city', 'state', 'zipcode')
    ordering = ('-created_at',)
    inlines = [OrderInline]
    actions = ['export_to_csv']

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="clients.csv"'
        
        writer = csv.writer(response)
        writer.writerow(['Full Name', 'Email', 'Phone', 'Address', 'City', 'State', 'Zipcode', 
                        'Total Orders', 'Total Spent', 'Created At'])
        
        for client in queryset:
            writer.writerow([
                client.full_name, client.email, client.phone, client.address,
                client.city, client.state, client.zipcode, client.total_orders,
                client.total_spent, client.created_at
            ])
        
        return response
    
    export_to_csv.short_description = "Export selected clients to CSV"

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'client', 'amount', 'status', 'order_date')
    list_filter = ('status', 'order_date')
    search_fields = ('order_number', 'client__full_name', 'description')
    ordering = ('-order_date',)

