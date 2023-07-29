const showPassword1 = document.querySelector("#togglePassword1");
const showPassword2 = document.querySelector("#togglePassword2");
const passwordField= document.querySelector("#password");
const confirmPassword = document.querySelector("#confirmpassword");

showPassword1.addEventListener("click", function(){
    // toggle the icon
    this.classList.toggle("fa-eye-slash");

    const type = passwordField.getAttribute("type") === "password" ? "text" : "password";
    passwordField.setAttribute("type", type);
    
})
showPassword2.addEventListener("click", function(){
    // toggle the icon
    this.classList.toggle("fa-eye-slash");
    // toggle the type attribute
    const type = confirmPassword.getAttribute("type") === "password" ? "text" : "password";
    confirmPassword.setAttribute("type", type);
})

