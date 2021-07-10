from django.contrib import admin
from clients.models import Order, OrderProduct


class OrderProductInline(admin.TabularInline):
    extra = 0
    model = OrderProduct
    raw_id_fields = ['order', ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'total', 'created_at']
    list_display_links = ['name', ]
    search_fields = ['name', ]
    raw_id_fields = ['client', ]

    inlines = [OrderProductInline, ]

    def name(self, obj):
        return obj.client.name
