document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    
    form.addEventListener("submit", function (e) {
        let valid = true;
        let messages = [];

        const name = document.getElementById("name").value.trim();
        const username = document.getElementById("username").value.trim();
        const age = parseInt(document.getElementById("age").value.trim());
        const height = parseFloat(document.getElementById("height").value.trim());
        const weight = parseFloat(document.getElementById("weight").value.trim());
        const email = document.getElementById("email").value.trim();
        const password = document.getElementById("password").value;
        const confirmPassword = document.getElementById("confirm_password").value;
        const fitnessLevel = document.getElementById("fitness_level").value;
        const photo = document.getElementById("photo").files[0];

        // Name & username
        if (name.length < 3) {
            valid = false;
            messages.push("Full name must be at least 3 characters.");
        }

        if (username.length < 3) {
            valid = false;
            messages.push("Username must be at least 3 characters.");
        }

        // Age
        if (isNaN(age) || age < 5 || age > 100) {
            valid = false;
            messages.push("Enter a valid age between 5 and 100.");
        }

        // Height
        if (isNaN(height) || height < 50 || height > 250) {
            valid = false;
            messages.push("Enter a valid height between 50cm and 250cm.");
        }

        // Weight
        if (isNaN(weight) || weight < 20 || weight > 300) {
            valid = false;
            messages.push("Enter a valid weight between 20kg and 300kg.");
        }

        // Email
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            valid = false;
            messages.push("Enter a valid email address.");
        }

        // Passwords
        if (password.length < 6) {
            valid = false;
            messages.push("Password must be at least 6 characters.");
        }

        if (password !== confirmPassword) {
            valid = false;
            messages.push("Passwords do not match.");
        }

        // Fitness Level
        if (fitnessLevel === "") {
            valid = false;
            messages.push("Please select a fitness level.");
        }

        // Photo check
        if (!photo || !photo.type.startsWith("image/")) {
            valid = false;
            messages.push("Please upload a valid image file.");
        }

        // Show alerts if invalid
        if (!valid) {
            e.preventDefault();
            alert(messages.join("\n"));
        }
    });
});

