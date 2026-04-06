function validatePolicyForm() {

    let policy_name = document.getElementById("policy_name").value.trim();
    let premium_amount = document.getElementById("premium_amount").value.trim();
    let duration_month = document.getElementById("duration_month").value.trim();

    let policy_name_error = document.getElementById('policy_name_error');
    let premium_amount_error = document.getElementById('premium_amount_error');
    let duration_month_error = document.getElementById('duration_month_error');

    let isValid = true;

    // Policy Name
    if (!policy_name) {
        policy_name_error.innerHTML = "Enter Policy Name";
        isValid = false;
    } else {
        policy_name_error.innerHTML = "";
    }

    // Premium Amount
    if (!premium_amount) {
        premium_amount_error.innerHTML = "Enter Premium Amount";
        isValid = false;
    } else if (isNaN(premium_amount) || Number(premium_amount) <= 0) {
        premium_amount_error.innerHTML = "Enter valid Premium Amount";
        isValid = false;
    } else {
        premium_amount_error.innerHTML = "";
    }

    // Duration Month
    if (!duration_month) {
        duration_month_error.innerHTML = "Enter Duration Month";
        isValid = false;
    } else if (isNaN(duration_month) || Number(duration_month) <= 0) {
        duration_month_error.innerHTML = "Enter valid Duration Month";
        isValid = false;
    } else {
        duration_month_error.innerHTML = "";
    }

    return isValid;
}


function confirmDelete() {
    console.log("grthgrth");
    
    return confirm("Are you sure you want to delete this customer?");
}

