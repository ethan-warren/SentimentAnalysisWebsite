window.onscroll = function() {myFunction()};
    
var navbar = document.getElementById("navBar");
var sticky = navbar.getBoundingClientRect().top;
var hero = document.getElementById("hero");
function myFunction() {
    if (window.scrollY >= sticky) {
    navbar.classList.add("sticky");
    hero.classList.add("navBarOffset");
    } else {
    navbar.classList.remove("sticky");
    hero.classList.remove("navBarOffset");
    }
}

window.addEventListener('resize', setSticky);
function setSticky() {
    /*sticky = navbar.getBoundingClientRect().top;
    myFunction(); */
}