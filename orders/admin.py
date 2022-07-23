from django.contrib import admin
from .models import Order

# Register your models here.
@admin.register(Order)
class OrderModel(admin.ModelAdmin):
    list_display = ['size','order_status','quantity','created_at']
    list_filter = ['size','order_status','created_at']
