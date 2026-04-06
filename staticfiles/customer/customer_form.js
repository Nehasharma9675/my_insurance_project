function validateForm() {

    let username = document.getElementById("username").value.trim();
    let password = document.getElementById("password").value.trim();
    let phone = document.getElementById("phone").value.trim();
    let city = document.getElementById("city").value.trim();
    let state = document.getElementById("state").value.trim();
    let kyc = document.getElementById("kyc_document").value;

    let usernameError = document.getElementById('usernameError');
    let passwordError = document.getElementById('passwordError');
    let phoneError = document.getElementById('phoneError');
    let cityError = document.getElementById('cityError');
    let stateError = document.getElementById('stateError');
    let kycError = document.getElementById('kycError');

    // Regex patterns
    let usernameRegex = /^[a-zA-Z0-9_]{3,20}$/;
    // let passwordRegex = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@!#$%^&*]{6,}$/;
    
    let phoneRegex = /^[0-9]{10}$/;
    let nameRegex = /^[A-Za-z ]{2,}$/;

    let isValid = true;
 
    // Username
    if (!usernameRegex.test(username)) {
        usernameError.innerHTML = "Username must be 3-20 characters (letters, numbers, _)";
        isValid = false;
    } else usernameError.innerHTML = "";

    // Password
    // if (!passwordRegex.test(password)) {
    //     passwordError.innerHTML = "Password must be 6+ chars with letters & numbers";
    //     isValid = false;
    // } else passwordError.innerHTML = "";

    // Phone
    if (!phoneRegex.test(phone)) {
        phoneError.innerHTML = "Enter valid 10-digit phone number";
        isValid = false;
    } else phoneError.innerHTML = "";

    // City
    if (!nameRegex.test(city)) {
        cityError.innerHTML = "Enter valid city name";
        isValid = false;
    } else cityError.innerHTML = "";

    // State
    if (!nameRegex.test(state)) {
        stateError.innerHTML = "Enter valid state name";
        isValid = false;
    } else stateError.innerHTML = "";

    // KYC
    if (kyc === "") {
        kycError.innerHTML = "Please upload KYC document";
        isValid = false;
    } else kycError.innerHTML = "";


    return isValid;
}

function confirmDelete() {
    console.log("grthgrth");
    
    return confirm("Are you sure you want to delete this customer?");
}

