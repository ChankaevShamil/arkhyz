// arkhyz_life/static/js/script.js

document.addEventListener('DOMContentLoaded', function() {
    // Логика для бургер-меню
    const burgerButton = document.querySelector('.burger-menu-button');
    const burgerMenu = document.getElementById('burgerMenu');
    const closeButton = document.querySelector('.burger-menu-close-button');
    const overlay = document.getElementById('overlay');

    if (burgerButton && burgerMenu) {
        burgerButton.addEventListener('click', function() {
            burgerMenu.classList.toggle('open');
            burgerButton.setAttribute('aria-expanded', burgerMenu.classList.contains('open'));
            if (overlay) overlay.classList.toggle('active');
        });
    }

    if (closeButton && burgerMenu) {
        closeButton.addEventListener('click', function() {
            burgerMenu.classList.remove('open');
            burgerButton.setAttribute('aria-expanded', 'false');
            if (overlay) overlay.classList.remove('active');
        });
    }

    if (overlay) {
        overlay.addEventListener('click', function() {
            burgerMenu.classList.remove('open');
            burgerButton.setAttribute('aria-expanded', 'false');
            overlay.classList.remove('active');
        });
    }

    // Простой лайтбокс (если не используется сторонняя библиотека)
    // Это ОЧЕНЬ упрощенный пример. Для полноценного лайтбокса лучше взять готовую библиотеку.
    const galleryItems = document.querySelectorAll('.gallery-item[data-lightbox]');
    if (galleryItems.length > 0) {
        const lightboxContainer = document.createElement('div');
        lightboxContainer.id = 'custom-lightbox';
        lightboxContainer.style.display = 'none';
        lightboxContainer.style.position = 'fixed';
        lightboxContainer.style.top = '0';
        lightboxContainer.style.left = '0';
        lightboxContainer.style.width = '100%';
        lightboxContainer.style.height = '100%';
        lightboxContainer.style.backgroundColor = 'rgba(0,0,0,0.8)';
        lightboxContainer.style.zIndex = '2000';
        lightboxContainer.style.justifyContent = 'center';
        lightboxContainer.style.alignItems = 'center';

        const lightboxImage = document.createElement('img');
        lightboxImage.style.maxWidth = '90%';
        lightboxImage.style.maxHeight = '90%';
        lightboxImage.style.boxShadow = '0 0 25px rgba(0,0,0,0.5)';

        lightboxContainer.appendChild(lightboxImage);
        document.body.appendChild(lightboxContainer);

        galleryItems.forEach(item => {
            item.addEventListener('click', function(event) {
                event.preventDefault();
                lightboxImage.src = this.href;
                lightboxContainer.style.display = 'flex';
            });
        });

        lightboxContainer.addEventListener('click', function() {
            this.style.display = 'none';
            lightboxImage.src = ''; // Clear src
        });
    }

});

// Если нужна инициализация для Lightbox2 (пример):
// lightbox.option({
//   'resizeDuration': 200,
//   'wrapAround': true
// })