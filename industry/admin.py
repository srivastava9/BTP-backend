from django.contrib import admin
from .models import *

# Register your models here.


class EmployeeInline(admin.TabularInline):
    model = Employee


class ProductInline(admin.TabularInline):
    model = Products


class ProductInventoryInline(admin.TabularInline):
    model = ProductInventory


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("type",)
    inlines = [ProductInline, EmployeeInline]


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("factory",)
    inlines = [ProductInventoryInline]
