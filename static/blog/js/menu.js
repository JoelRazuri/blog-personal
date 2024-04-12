let d = document;
let userMenuButton = d.getElementById('user-menu-button');
let userMenu = d.getElementById('user-menu');


const menuToggle = () => {
    const closeMenu = (event) => {
        if (!userMenu.contains(event.target) && !userMenuButton.contains(event.target)) {
            userMenu.classList.add("hidden");
            userMenuButton.classList.remove("focus:ring-offset-red-400");
            document.removeEventListener('click', closeMenu);
        }
    };

    const openMenu = () => {
        userMenu.classList.toggle("hidden");
        userMenuButton.classList.toggle("focus:ring-offset-red-400");
        document.addEventListener('click', closeMenu);
    };

    userMenuButton.addEventListener('click', (event) => {
        event.stopPropagation();
        openMenu();
    });
};

menuToggle();


