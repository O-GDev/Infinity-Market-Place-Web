
function reveal() {
  var reveals = document.querySelectorAll(".reveal");

  for (var i = 0; i < reveals.length; i++) {
    var windowHeight = window.innerHeight;
    var elementTop = reveals[i].getBoundingClientRect().top;
    var elementVisible = 150;

    if (elementTop < windowHeight - elementVisible) {
      reveals[i].classList.add("active");
    } else {
      reveals[i].classList.remove("active");
    }
  }
}

window.addEventListener("scroll", reveal);


function myFunction() {
  document.getElementById("phone-menus").style.display = "block";
  document.getElementById("menu-icon-id").style.display = "none";
  document.getElementById("menu-close-icon").style.display = "block";
}
function closeNav(){
  document.getElementById("phone-menus").style.display = "none";
  document.getElementById("menu-icon-id").style.display = "block";
  document.getElementById("menu-close-icon").style.display = "none";  
}
