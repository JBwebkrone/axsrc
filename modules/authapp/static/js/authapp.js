
// signup show and hide password start
var eyeSlash1 = document.getElementById("eye-slash1");
var withoutSlash1 = document.getElementById("without-slash1");

var eyeSlash2 = document.getElementById("eye-slash2");
var withoutSlash2 = document.getElementById("without-slash2");

var password1 = document.getElementById("password1");
var password2 = document.getElementById("password2");

// for password1 start
eyeSlash1.addEventListener("click", () => {
    eyeSlash1.classList.add("d-none");
    withoutSlash1.classList.remove("d-none");
    password1.type = "text";
});

withoutSlash1.addEventListener("click", () => {
    withoutSlash1.classList.add("d-none");
    eyeSlash1.classList.remove("d-none");
    password1.type = "password";
});
// for password1 end

// for password2 start
eyeSlash2.addEventListener("click", () => {
    eyeSlash2.classList.add("d-none");
    withoutSlash2.classList.remove("d-none");
    password2.type = "text";
});

withoutSlash2.addEventListener("click", () => {
    withoutSlash2.classList.add("d-none");
    eyeSlash2.classList.remove("d-none");
    password2.type = "password";
});
// for password2 end

// signup show and hide password end


// email phone validation start
var emailPhone = document.getElementById("email-phone");

emailPhone.addEventListener("input", () => {
    var emailPhoneValue = emailPhone.value;
    if(/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(emailPhoneValue) || /^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/.test(emailPhoneValue) ){
        emailPhone.style.borderColor = "green";
        console.log("Success");
    } else {
        emailPhone.style.borderColor = "red";
        console.log("Failure");
    }

});
// email phone validation end

