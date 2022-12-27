from django.contrib import admin

from .models import *

@admin.register(Risk)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'quantity', 'description')
    list_filter = ('name', 'price')
    raw_id_fields = ('category', 'subcategory')
    search_fields = ('name', 'price')
    list_editable = ('price', 'quantity')
    save_on_top = True
    save_as = True
    fieldsets = (
        ('Настройка отображения товара', {
            'fields': (('name', 'description', 'price', 'quantity', 'image_1'),)
        }),
        ('Настройки категории', {
            'fields': ('category', 'subcategory',)
        }),
        ('Изображения', {
                     'classes': ('collapse',),
                     'fields': (('image_2', 'image_3', 'image_4', 'image_5', 'image_6', 'image_7', 'image_8',
                                 'image_9', 'image_10',),)
                 }),
    )
