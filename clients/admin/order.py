from django.contrib import admin
from clients.models import OrderItems, Order, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


class ItensDoPedidoInline(admin.TabularInline):
    extra = 0
    model = OrderItems
    raw_id_fields = ['product', ]
    # inlines = [PedidoAdmin,]


@admin.register(Order)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['pk', 'client',]

    inlines = [ItensDoPedidoInline,]
