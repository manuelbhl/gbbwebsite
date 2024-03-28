
//const toggleButton = document.getElementsByClassName('toggle-button')[0];
//const navbarLinks = document.getElementsByClassName('navbar-links')[0];
//alert(navbarLinks);
//toggleButton.addEventListner('click', () => {

//navbarLinks.classList.toggle('active')

const toggleButton = document.querySelector(".toggle-button");

const navbarLinks = document.querySelector(".navbar-links");
toggleButton.addEventListener("click", function()
{

//menu.classList.toggle("is-active");
navbarLinks.classList.toggle("active");

});
 