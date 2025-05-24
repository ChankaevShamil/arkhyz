# arkhyz_life/arkhyz_life/urls.py

from django.contrib import admin
from django.urls import path, include # Добавь include
from django.conf import settings # Добавь это
from django.conf.urls.static import static # Добавь это

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls')), # Подключаем URL-ы нашего приложения catalog
                                        # Пустой префикс '' означает, что URL-ы из catalog.urls
                                        # будут доступны прямо с корня сайта (например, /category/konnie-tury/)
]

# Эта часть нужна только в режиме DEBUG (т.е. для разработки)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Можно также добавить для статики, хотя для статики runserver обычно и так работает
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # Но для STATIC_ROOT нужно еще его определить и запустить collectstatic, для разработки обычно хватает STATICFILES_DIRS
