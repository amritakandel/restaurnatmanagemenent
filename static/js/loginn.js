// script.js

document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting the traditional way

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Add your authentication logic here
    if (username === 'user' && password === 'pass') {
        alert('Login successful!');
    } else {
        alert('Invalid username or password');
    }
});


