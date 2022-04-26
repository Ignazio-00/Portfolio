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
// EventHandler.on(document, clickEvent, '[data-bs-dismiss="{alert}"]')

function change(){
    document.getElementById("btn-danger").className = "close"
}

// 
document.getElementById("btn-danger").addEventListener('click', change) 

