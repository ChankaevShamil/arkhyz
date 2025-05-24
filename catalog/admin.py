# arkhyz_life/catalog/admin.py
from django.contrib import admin
from .models import Category, Provider, ProviderImage

class ProviderImageInline(admin.TabularInline): # или admin.StackedInline
    model = ProviderImage
    extra = 1 # Количество пустых форм для добавления новых изображений галереи
    verbose_name = "Изображение галереи"
    verbose_name_plural = "Изображения галереи"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'subtitle', 'slug')
    prepopulated_fields = {'slug': ('name',)} # Автозаполнение slug из name
    search_fields = ['name', 'subtitle']

@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'slug')
    list_filter = ('categories',) # Фильтр по категориям
    search_fields = ('name', 'short_description', 'full_description', 'phone_number')
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ('categories',) # Удобный интерфейс для ManyToMany (выбор категорий)
    inlines = [ProviderImageInline] # Встраивание управления галереей изображений прямо в форму провайдера

# ProviderImage будет управляться через ProviderAdmin с помощью инлайна,
# поэтому отдельно регистрировать ProviderImageAdmin обычно не нужно,
# если только не требуется отдельный доступ к списку всех изображений.
# Если нужно, можно так:
# @admin.register(ProviderImage)
# class ProviderImageAdmin(admin.ModelAdmin):
#     list_display = ('provider', 'image', 'sort_order')
#     list_filter = ('provider',)