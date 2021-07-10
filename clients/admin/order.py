from django.contrib import admin
from clients.models import Order, Product, People, OrderProduct

#
# @admin.register(Order, Product)
# class ProductAdmin(admin.ModelAdmin):
#     # list_display = ['name', 'price', 'description']
#     # extra = 0
#     # model = Product
#     # raw_id_fields = ['order', ]
#     pass


class OrderProductInline(admin.TabularInline):
    extra = 0
    model = OrderProduct
    raw_id_fields = ['order', ]


# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ['name', ]
#     inlines = [ProductAdmin]
#     # raw_id_fields = ['client', ]

@admin.register(Order)
class MainOrderAdmin(admin.ModelAdmin):
    raw_id_fields = ['client', ]

    inlines = [OrderProductInline, ]




@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    search_fields = ['name', 'cpf', 'rg']
    fieldsets = (
        ('Person data', {
            'fields': (
                'name',
                'cpf',
                'rg',
                'birth_date',
                'age',
            )
        }),
        ('Contacts', {
           'fields':(
               'email',
               'telefone_number',
               'mobile',
           )
        }),
        ('Others', {
            'fields': (
                'sex',
                'mother_name',
                'father_name',
                'sign',
                'height',
                'weight',
                'type_blood',
                'favorite_color',
            )

        })
    )
