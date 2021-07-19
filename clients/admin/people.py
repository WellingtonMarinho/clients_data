from django.contrib import admin
from clients.models import People


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    search_fields = ['name', 'cpf', 'rg']
    list_display = ['pk', 'name', 'age', 'email']
    list_display_links = ['name', ]
    fieldsets = (
        ('Person data', {
            'fields': (
                'name',
                'cpf',
                'rg',
                'birth_date',
                'age',
                'age_group'
            )
        }),
        ('Contacts', {
            'classes': ('collapse',),
            'fields':(
               'email',
               'telefone_number',
               'mobile',
           )
        }),
        ('Others', {
            'classes': ('collapse',),
            'fields': (
                'sex',
                'mother_name',
                'father_name',
                'sign',
                'height',
                'weight',
                'imc',
                'type_blood',
                'favorite_color',
            )

        })
    )
    readonly_fields = ['age', 'imc', 'age_group']
