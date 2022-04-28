// Scroll to top selection
const scrollUp = document.querySelector("#scroll-up");

// Select nav links
const navLink = document.querySelectorAll(".nav-link");

// Hamburger Menu
const btn = document.getElementById("menu-btn")
const nav = document.getElementById("menu")

function navToggle() {
    btn.classList.toggle("open")
    nav.classList.toggle("hidden")
    document.body.classList.toggle("no-scroll")
}

btn.addEventListener("click", navToggle)

// Dropdown menu posts
const SELECTOR_DROPDOWN_TOGGLE = '.dropdown-toggle';

// Alert handling
document.querySelectorAll(".btnf-close").forEach(element => {
    element.addEventListener('click', function(event){
        event.target.parentElement.remove()
    })
});