from django.contrib import admin

from shopping_list.models import ShoppingItem


@admin.register(ShoppingItem)
class ShoppingItemAdmin(admin.ModelAdmin):
    search_fields = ("id", "name")
    list_display = ("id", "name", "purchased")
    list_filter = ("purchased",)
