from django.contrib import admin
from clients.models import Order, Product, People


class ProductAdmin(admin.TabularInline):
    extra = 0
    # fields = '__all__'
    model = Product
    # raw_id_fields = ['order', ]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # list_display = ['client', ]
    # inlines = [ProductAdmin]
    # raw_id_fields = ['client', ]
    pass


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
