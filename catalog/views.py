# arkhyz_life/catalog/views.py

from django.shortcuts import render, get_object_or_404
from .models import Category, Provider # Импортируем наши модели

# Вспомогательная функция или общий контекст для передачи категорий во все шаблоны (для бургер-меню)
def get_common_context():
    return {
        'all_categories': Category.objects.all().order_by('name') # Получаем все категории для меню
    }

# 1. Главная страница (фото 1)
def home_page(request):
    context = get_common_context()
    # Дополнительный контекст для главной страницы, если нужен
    # context['some_featured_items'] = ...
    return render(request, 'catalog/home.html', context)

# 2. Страница списка категорий (если нужна отдельная страница для фото 2)
def category_list_page(request):
    # Категории уже есть в get_common_context(), поэтому просто передаем его
    context = get_common_context()
    # context['page_title'] = "Все категории услуг" # Можно добавить заголовок
    return render(request, 'catalog/category_list_page.html', context)


# 3. Страница Списка Провайдеров в выбранной Категории (фото 3)
def provider_list_page(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    # Получаем всех провайдеров, которые принадлежат этой категории
    # related_name='providers' в модели Category позволяет это сделать так:
    providers_in_category = category.providers.all().order_by('name')

    context = get_common_context()
    context.update({
        'current_category': category,
        'providers': providers_in_category,
    })
    return render(request, 'catalog/provider_list_page.html', context)

# 4. Детальная страница Провайдера (фото 4)
def provider_detail_page(request, provider_slug):
    provider = get_object_or_404(Provider, slug=provider_slug)
    # Галерея изображений уже связана с провайдером через related_name='gallery_images'
    # и будет доступна в шаблоне как provider.gallery_images.all

    context = get_common_context()
    context.update({
        'provider': provider,
    })
    return render(request, 'catalog/provider_detail_page.html', context)