const passwordBox = document.querySelector(".password-box");
const passwordInput = passwordBox.querySelector("input")
const passwordToggleBox = document.querySelector(".password-toggle");
const eyeElement = passwordToggleBox.querySelector("i");

passwordToggleBox.addEventListener("click", () => {
    

    if (eyeElement.classList.contains("fa-eye-slash")){

        // Update Eye
        eyeElement.classList.remove("fa-eye-slash");
        eyeElement.classList.add("fa-eye");

        // Update input
        passwordInput.setAttribute("type" , "password");
        
    }
    else{

        // Update Eye
        eyeElement.classList.remove("fa-eye");
        eyeElement.classList.add("fa-eye-slash");
    
        // Update input
        passwordInput.setAttribute("type" , "text");

    }

});
