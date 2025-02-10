from django.contrib import admin
from .models import Customer, MenuItem, Order, OrderItem

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'created_at')
    list_filter = ('created_at', 'email', 'phone_number', 'name')
    search_fields = ('name', 'email', 'phone_number')

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'category', 'available')
    list_filter = ('category', 'available', 'name')
    search_fields = ('name', 'description')

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'menu_item', 'quantity')
    list_filter = ('quantity',)
    search_fields = ('order__customer__name', 'menu_item__name')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'status', 'created_at')
    list_filter = ('created_at', 'status')
    search_fields = ('customer__name', 'status')


admin.site.register(Customer, CustomerAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)

