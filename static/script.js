// Toggle Hamburger Menu
function toggleHamburgerMenu() {
    const hamburgerMenu = document.querySelector('.hamburger-menu');
    const navbar = document.querySelector('.navbar');
    const searchForm = document.querySelector('.search-form');
    const langSwitcher = document.querySelector('.lang-switcher');

    hamburgerMenu.classList.toggle('active');
    navbar.classList.toggle('active');
    searchForm.classList.toggle('active');
    langSwitcher.classList.toggle('active');
    document.body.classList.toggle('menu-open');
}

// Initialize Swiper Slider
function initializeSwiper() {
    const swiper = new Swiper('.swiper-container', {
        slidesPerView: 1,
        spaceBetween: 30,
        loop: false,
        slideToClickedSlide: true,

        pagination: {
            el: '.swiper-pagination',
            clickable: true,
            dynamicBullets: true,
        },

        navigation: {
            nextEl: '.right-btn',
            prevEl: '.left-btn',
        },

        on: {
            slideChange: function () {
                document.querySelector('.left-btn').disabled = this.isBeginning;
                document.querySelector('.right-btn').disabled = this.isEnd;
            },
        },

        breakpoints: {
            0: { slidesPerView: 1 },
            768: { slidesPerView: 2 },
            1024: { slidesPerView: 3 },
        },
    });

    // Initial button state
    document.querySelector('.left-btn').disabled = swiper.isBeginning;
    document.querySelector('.right-btn').disabled = swiper.isEnd;
}

// Close Menu and Scroll to Section
function setupNavbarLinks() {
    const navbarLinks = document.querySelectorAll('.navbar ul li a');
    const hamburgerMenu = document.querySelector('.hamburger-menu');
    const navbar = document.querySelector('.navbar');
    const searchForm = document.querySelector('.search-form');
    const langSwitcher = document.querySelector('.lang-switcher');
    const productsLink = document.querySelector('a[href="#products"]');

    navbarLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();

            const targetId = link.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);

            if (targetElement) {
                targetElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }

            // Close the menu
            hamburgerMenu.classList.remove('active');
            navbar.classList.remove('active');
            searchForm.classList.remove('active');
            langSwitcher.classList.remove('active');
            document.body.classList.remove('menu-open');
        });
    });

     // Close the menu and scroll to the "محصولات" section when clicking on the "محصولات" link
     productsLink.addEventListener('click', function (e) {
        e.preventDefault();

        // Close the menu
        hamburgerMenu.classList.remove('active');
        navbar.classList.remove('active');
        searchForm.classList.remove('active');
        langSwitcher.classList.remove('active');
        document.body.classList.remove('menu-open');

        const targetElement = document.getElementById('products');

        if (targetElement) {
            targetElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });
}

// Close Navbar When Clicking Outside
function setupOutsideClickListener() {
    document.addEventListener('click', (event) => {
        const navbar = document.querySelector('.navbar');
        const burger = document.querySelector('.hamburger-menu');
        const searchForm = document.querySelector('.search-form');
        const langSwitcher = document.querySelector('.lang-switcher');

        if (!navbar.contains(event.target) && !burger.contains(event.target) && !searchForm.contains(event.target)) {
            burger.classList.remove('active');
            navbar.classList.remove('active');
            searchForm.classList.remove('active');
            langSwitcher.classList.remove('active');
            document.body.classList.remove('menu-open');
        }
    });
}

// Animate Slogan Text
function animateSloganText() {
    const slogan = document.querySelector('.slogan-section h1');
    const text = slogan.textContent;
    slogan.textContent = '';

    text.split('').forEach((char, i) => {
        const span = document.createElement('span');
        span.textContent = char;
        span.style.animationDelay = `${i * 50}ms`;
        slogan.appendChild(span);
    });
}

// Initialize All Functions on DOMContentLoaded
document.addEventListener('DOMContentLoaded', () => {
    console.log('Welcome to Your Website!');

    initializeSwiper();
    setupNavbarLinks();
    setupOutsideClickListener();
    animateSloganText();
});

function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(function() {
        alert("🔗 Link copied to clipboard!");
    }).catch(function(error) {
        console.error("Copy failed:", error);
    });
}




