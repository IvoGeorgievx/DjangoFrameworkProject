from django.contrib import admin

from project_watches.web.models import Watches, Sunglasses, Wallets, Belts, Ties


@admin.register(Watches)
class WatchesAdmin(admin.ModelAdmin):
    list_display = ('name', 'year')
    ordering = ('year',)
    list_filter = ('year',)
    search_fields = ('name__startswith',)
    list_per_page = 5


@admin.register(Sunglasses)
class SunglassesAdmin(admin.ModelAdmin):
    list_display = ('name', 'lens_size', 'frame_type', 'price',)
    ordering = ('name', 'price',)
    list_filter = ('price', 'lens_size',)
    search_fields = ('price__startswith', 'lens_size__startswith', 'lens_color__startswith',)
    list_per_page = 5


@admin.register(Wallets)
class WalletsAdmin(admin.ModelAdmin):
    list_display = ('name', 'card_capacity', 'price',)
    ordering = ('name', 'card_capacity', 'price',)
    list_filter = ('price', 'card_capacity')
    search_fields = ('price__startswith',)
    list_per_page = 5


@admin.register(Belts)
class BeltsAdmin(admin.ModelAdmin):
    list_display = ('brand', 'color', 'price',)
    ordering = ('brand', 'price', 'color',)
    list_filter = ('price', 'color', 'buckle_form',)
    search_fields = ('price__startswith', 'color__startswith',)
    list_per_page = 5


@admin.register(Ties)
class TiesAdmin(admin.ModelAdmin):
    list_display = ('brand', 'color', 'price',)
    ordering = ('brand', 'price', 'color',)
    list_filter = ('price', 'color', 'material',)
    search_fields = ('price__startswith', 'color__startswith', 'material__startswith',)
    list_per_page = 5



