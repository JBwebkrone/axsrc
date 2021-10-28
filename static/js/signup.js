
// signup show and hide password start
var eyeSlash1 = document.getElementById("eye-slash1");
var withoutSlash1 = document.getElementById("without-slash1");

var eyeSlash2 = document.getElementById("eye-slash2");
var withoutSlash2 = document.getElementById("without-slash2");

var password = document.getElementById("id_password");
var password1 = document.getElementById("id_password1");

var firstName = document.getElementById("id_first_name");
var lastName = document.getElementById("id_last_name");

// for password1 start
eyeSlash1.addEventListener("click", () => {
    eyeSlash1.classList.add("d-none");
    withoutSlash1.classList.remove("d-none");
    password.type = "text";
});

withoutSlash1.addEventListener("click", () => {
    withoutSlash1.classList.add("d-none");
    eyeSlash1.classList.remove("d-none");
    password.type = "password";
});
// for password1 end

// for password2 start
eyeSlash2.addEventListener("click", () => {
    eyeSlash2.classList.add("d-none");
    withoutSlash2.classList.remove("d-none");
    password1.type = "text";
});

withoutSlash2.addEventListener("click", () => {
    withoutSlash2.classList.add("d-none");
    eyeSlash2.classList.remove("d-none");
    password1.type = "password";
});
// for password2 end

// signup show and hide password end


// email phone validation start
var email = document.getElementById("id_email");
var phone = document.getElementById("id_phone");
var emailPattern = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
var phonePattern = /^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/

email.addEventListener("input", () => {
    var emailValue = email.value;
    if(emailPattern.test(emailValue) ){
        email.style.borderColor = "green";
        console.log("Success");
    } else {
        email.style.borderColor = "red";
        console.log("Failure");
    }

});

phone.addEventListener("input", () => {
    var phoneValue = phone.value;
    if(phonePattern.test(phoneValue)){
        phone.style.borderColor = "green";
        console.log("Success");
    } else {
        phone.style.borderColor = "red";
        console.log("Failure");
    }

});
// email phone validation end


// MATCH PASSWORD AND PASSWORD1
password.addEventListener("input", () => {
    if(password.value !== password1.value){
        document.getElementById("passwordError").innerHTML = "Password doen't match";
        password.style.borderColor = "red";
        password1.style.borderColor = "red";
    }
    else{
        document.getElementById("passwordError").innerHTML = "";
        password.style.borderColor = "green";
        password1.style.borderColor = "green";
    }
});

password1.addEventListener("input", () => {
    if(password1.value !== password.value){
        document.getElementById("passwordError").innerHTML = "Password doen't match";
        password.style.borderColor = "red";
        password1.style.borderColor = "red";
    }
    else{
        document.getElementById("passwordError").innerHTML = "";
        password.style.borderColor = "green";
        password1.style.borderColor = "green";
    }
});


// first name && last name length validation start
firstName.addEventListener("input", () => {
    if(firstName.value.length === 1){
        document.getElementById("firstName").innerHTML = "First name should have more than 1 character";
        firstName.style.borderColor = "red";
    }
    else{
        document.getElementById("firstName").innerHTML = "";
        firstName.style.borderColor = "green";
    }
});


lastName.addEventListener("input", () => {
    if(lastName.value.length === 1){
        document.getElementById("lastName").innerHTML = "Last name should have more than 1 character";
        lastName.style.borderColor = "red";
    }
    else{
        document.getElementById("lastName").innerHTML = "";
        lastName.style.borderColor = "green";
    }
});
// first name && last name length validation end