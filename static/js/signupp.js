// script.js

document.getElementById('signupForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting the traditional way

    const username = document.getElementById('signupUsername').value;
    const email = document.getElementById('signupEmail').value;
    const password = document.getElementById('signupPassword').value;

    // Add your signup logic here
    if (username && email && password) {
        alert('Signup successful!');
    } else {
        alert('Please fill out all fields.');
    }
});
