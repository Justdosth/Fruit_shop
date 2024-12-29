// import Swiper from 'swiper/bundle';
// import 'swiper/swiper-bundle.min.css';


document.addEventListener('DOMContentLoaded', () => {
    console.log('Welcome to Your Website!');
    // JavaScript for Slider
    new Swiper('.swiper-container', {
        loop: true,
        spaceBetween: 30,
    
        // Pagination bullets
        pagination: {
        el: '.swiper-pagination',
        clickable: true,
        dynamicBullets: true,
        },
    
        // Navigation arrows
        navigation: {
        nextEl: '.right-btn',
        prevEl: '.left-btn',
        },

        // Responsive breakpoints
        breakpoints:{
        0: {
            slidesPerView: 1
            },
        768: {
            slidesPerView: 2
            },
        1024: {
            slidesPerView: 3
            },
        }
    
    });
});

document.addEventListener('DOMContentLoaded', () => {
    const slogan = document.querySelector('.slogan-section h1');
    const text = slogan.textContent;
    slogan.textContent = '';

    text.split('').forEach((char, i) => {
        const span = document.createElement('span');
        span.textContent = char;
        span.style.animationDelay = `${i * 50}ms`;
        slogan.appendChild(span);
    });
});





// function updateSlider() {
//     const slider = document.querySelector('.slider');
//     const cardWidth = slider.querySelector('.service-card').offsetWidth;
//     const gap = 20; // Adjust if needed
//     slider.style.transform = 'translateX(-${(cardWidth + gap) * currentSlide}px)';
// }

// function nextSlide() {
//     const slider = document.querySelector('.slider');
//     const totalCards = slider.children.length;
//     const visibleCards = Math.floor(slider.parentElement.offsetWidth / slider.querySelector('.service-card').offsetWidth);
//     if (currentSlide < totalCards - visibleCards) {
//         currentSlide++;
//     } else {
//         currentSlide = 0; // Loop to start
//     }
//     updateSlider();
// }

// function prevSlide() {
//     const slider = document.querySelector('.slider');
//     if (currentSlide > 0) {
//         currentSlide--;
//     } else {
//         currentSlide = slider.children.length - 1; // Loop to last
//     }
//     updateSlider();
// }
