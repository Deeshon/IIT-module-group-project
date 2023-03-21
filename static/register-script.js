const registerBtn = document.querySelector("#register")
registerBtn.addEventListener("click", (event) => {
    const password = document.querySelector("#password")
    const confirmPassword = document.querySelector("#confirm-password")

    if (password.value !== confirmPassword.value) {
        event.preventDefault()
        alert("Password does not match")
    }

})