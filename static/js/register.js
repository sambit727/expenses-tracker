const username = document.getElementById('usernameInput');
const usernameFeedback = document.querySelector('.invalid-feedback');
const usernameSuccessOutput = document.querySelector('.usernameSuccessOutput');

const email = document.getElementById('emailInput');
const emailFeedback = document.querySelector('.emailFeedbackArea');

const passwordField1 = document.querySelector('#passwordInput1');
const passwordFeedback1= document.querySelector('.passwordFeedbackArea1');

const passwordField2 = document.querySelector('#passwordInput2');
const showPasswordToggle = document.querySelector('.showPasswordToggle');
const passwordFeedback2 = document.querySelector('.passwordFeedbackArea2');

const submitButton = document.querySelector('#submit-btn');




const handleToggleInput = (e) => {
    if(showPasswordToggle.textContent === "Show") {
        showPasswordToggle.textContent = "Hide";
        passwordField2.type = "text";
    }else{
        showPasswordToggle.textContent = "Show";
        passwordField2.type = "password";
    }
};
showPasswordToggle.addEventListener("click", handleToggleInput);



passwordField1.addEventListener("keyup", (e) => {
    const passwordVal = e.target.value

    if(passwordVal.length>=0) {
        fetch("/validate-password/", {
            body:JSON.stringify({ password: passwordVal }),
            method: "POST",
        })
        .then(response=>response.json())
        .then(data=>{
            if(data.password_error) {
                passwordField1.classList.add("is-invalid");
                passwordFeedback1.style.display = "block";
                passwordFeedback1.innerHTML = `<p>${data.password_error}</p>`
                submitButton.disabled = true;
            }
            if(data.password_valid) {
                passwordField1.classList.remove("is-invalid");
                passwordField1.classList.add("is-valid");
                passwordFeedback1.style.display = "none";
                submitButton.disabled = false;
            }
        })
    }
});



passwordField2.addEventListener("keyup", (e) => {
    const passwordVal = passwordField1.value
    const passwordCheckVal = e.target.value
    if(passwordCheckVal !== passwordVal) {
        passwordField2.classList.add("is-invalid");
        passwordFeedback2.style.display = "block";
        passwordFeedback2.innerHTML = `<p>Password does not match</p>`
        submitButton.disabled = true;
    }else{
        passwordField2.classList.remove("is-invalid");
        passwordField2.classList.add("is-valid");
        passwordFeedback2.style.display = "none";
        submitButton.disabled = false;
    }
});



email.addEventListener("keyup", (e) => {
    const emailVal = e.target.value

    if(emailVal.length>=0) {
        // email.classlist.remove("is-invalid")
        fetch("/validate-email/", {
            body:JSON.stringify({ email: emailVal }),
            method: "POST",
        })
        .then(response=>response.json())
        .then(data=>{
            if(data.email_error) {
                email.classList.add("is-invalid");
                emailFeedback.style.display = "block";
                emailFeedback.innerHTML = `<p>${data.email_error}</p>`
                submitButton.disabled = true;
            }
            if(data.email_valid) {
                email.classList.remove("is-invalid");
                email.classList.add("is-valid");
                emailFeedback.style.display = "none";
                submitButton.disabled = false;
            }
        })
    }
});



username.addEventListener('keyup', (e) => {
    const usernameVal = e.target.value
    
    if(usernameVal.length>=0) {
        usernameSuccessOutput.style.display="block"
        fetch("/validate-username/", {
            body:JSON.stringify({ username: usernameVal }),
            method: "POST",
        })
        .then(response=>response.json())
        .then(data=>{
            usernameSuccessOutput.style.display="none"
            if(data.username_error) {
                username.classList.add("is-invalid");
                usernameFeedback.style.display = "block";
                usernameFeedback.innerHTML = `<p>${data.username_error}</p>`
                submitButton.disabled = true;
            }
            if(data.username_valid) {
                username.classList.remove("is-invalid");
                username.classList.add("is-valid");
                usernameFeedback.style.display = "none";
                submitButton.disabled = false;
            }
        })
    }
})