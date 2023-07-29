const showPassword1 = document.querySelector("#togglePassword1");
const showPassword2 = document.querySelector("#togglePassword2");
const passwordField= document.querySelector("#new-password");
const confirmPassword = document.querySelector("#confirm-new-password");

showPassword1.addEventListener("click", function(){
    // toggle the icon
    this.classList.toggle("fa-eye2-slash");

    const type = passwordField.getAttribute("type") === "password" ? "text" : "password";
    passwordField.setAttribute("type", type);
    
})
showPassword2.addEventListener("click", function(){
    // toggle the icon
    this.classList.toggle("fa-eye2-slash");
    // toggle the type attribute
    const type = confirmPassword.getAttribute("type") === "password" ? "text" : "password";
    confirmPassword.setAttribute("type", type);
})