// Registration form handler for Sehat Setu

const API_BASE_URL = 'http://localhost:8000';

document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('.auth-form');
    if (!form) return;

    form.addEventListener('submit', async function (e) {
        e.preventDefault();
        
        const inputs = form.querySelectorAll('input[type="text"], input[type="tel"], input[type="email"], input[type="password"]');
        const fullName = inputs[0].value.trim();
        const phone = inputs[1].value.trim();
        const email = inputs[2].value.trim();
        const city = inputs[3].value.trim();
        const password = inputs[4].value;

        if (!fullName || !email || !password) {
            alert('Please fill in all required fields.');
            return;
        }

        // Split full name into first and last name
        const nameParts = fullName.split(' ');
        const firstName = nameParts[0];
        const lastName = nameParts.slice(1).join(' ') || '';

        try {
            const response = await fetch(`${API_BASE_URL}/api/auth/register/`, {
                method: 'POST',
                credentials: 'include',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    username: email.split('@')[0], // Use email prefix as username
                    email: email,
                    password: password,
                    first_name: firstName,
                    last_name: lastName,
                    phone_number: phone,
                    city: city,
                    user_type: 'patient'
                })
            });
            
            const data = await response.json();
            
            if (response.ok) {
                alert('Registration successful! Redirecting to dashboard...');
                // Store user data
                localStorage.setItem('currentUser', JSON.stringify(data.user));
                localStorage.setItem('userId', data.user.id);
                window.location.href = 'dashboard.html';
            } else {
                alert(data.error || 'Registration failed.');
            }
        } catch (err) {
            console.error('Error:', err);
            alert('Could not connect to server. Make sure Django is running on port 8000.');
        }
    });
});
