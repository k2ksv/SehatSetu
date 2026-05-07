// Login form handler for Sehat Setu

const API_BASE_URL = 'http://localhost:8000';

document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('.auth-form');
    if (!form) return;

    form.addEventListener('submit', async function (e) {
        e.preventDefault();
        
        const inputs = form.querySelectorAll('input[type="text"], input[type="password"]');
        const usernameOrEmail = inputs[0].value.trim();
        const password = inputs[1].value;

        if (!usernameOrEmail || !password) {
            alert('Please enter username/email and password.');
            return;
        }

        try {
            const response = await fetch(`${API_BASE_URL}/api/auth/login/`, {
                method: 'POST',
                credentials: 'include',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    username: usernameOrEmail,
                    password: password
                })
            });
            
            const data = await response.json();
            
            if (response.ok) {
                alert('Login successful! Redirecting to dashboard...');
                // Store user data
                localStorage.setItem('currentUser', JSON.stringify(data.user));
                localStorage.setItem('userId', data.user.id);
                window.location.href = 'dashboard.html';
            } else {
                alert(data.error || 'Login failed. Invalid credentials.');
            }
        } catch (err) {
            console.error('Error:', err);
            alert('Could not connect to server. Make sure Django is running on port 8000.');
        }
    });
});
