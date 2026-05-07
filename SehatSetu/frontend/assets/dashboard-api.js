// API helper for dashboard
const API_BASE_URL = 'http://localhost:8000';

// Get current logged-in user
async function getCurrentUser() {
    try {
        const response = await fetch(`${API_BASE_URL}/api/auth/current-user/`, {
            method: 'GET',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
            }
        });
        
        if (!response.ok) {
            console.log('User not logged in');
            return null;
        }
        
        const data = await response.json();
        return data.user;
    } catch (err) {
        console.error('Error fetching current user:', err);
        return null;
    }
}

// Fetch all users from database
async function fetchUsers() {
    try {
        const response = await fetch(`${API_BASE_URL}/api/users/`, {
            method: 'GET',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
            }
        });
        
        if (!response.ok) throw new Error('Failed to fetch users');
        
        const data = await response.json();
        return data.users || [];
    } catch (err) {
        console.error('Error fetching users:', err);
        return [];
    }
}

// Render users in dashboard
function renderUsers(users) {
    const container = document.getElementById('user-list');
    if (!container) return;
    
    if (users.length === 0) {
        container.innerHTML = '<li>No users registered yet</li>';
        return;
    }
    
    container.innerHTML = users.slice(0, 5).map(user => `
        <li><strong>${user.name}</strong> <small>(${user.user_type})</small></li>
    `).join('');
}

// Display current user greeting
function displayUserGreeting(user) {
    const heading = document.querySelector('.dashboard-main h1');
    if (heading && user) {
        const firstName = user.first_name || 'User';
        heading.textContent = `Good afternoon, ${firstName}`;
    }
}

// Store user in localStorage for easy access
function storeCurrentUser(user) {
    if (user) {
        localStorage.setItem('currentUser', JSON.stringify(user));
        localStorage.setItem('userId', user.id);
    }
}

// Get user from localStorage
function getCurrentUserFromStorage() {
    const userStr = localStorage.getItem('currentUser');
    return userStr ? JSON.parse(userStr) : null;
}

// Initialize dashboard on load
async function initializeDashboard() {
    try {
        // Get current user
        const currentUser = await getCurrentUser();
        
        if (currentUser) {
            // Store user data
            storeCurrentUser(currentUser);
            
            // Display user greeting
            displayUserGreeting(currentUser);
            
            // Fetch and display all users
            const users = await fetchUsers();
            renderUsers(users);
        } else {
            // Redirect to login if not authenticated
            console.log('Redirecting to login...');
            // Uncomment next line to redirect if user not logged in
            // window.location.href = 'login.html';
        }
    } catch (err) {
        console.error('Error initializing dashboard:', err);
    }
}

// On dashboard load, initialize everything
if (window.location.pathname.endsWith('dashboard.html') || document.querySelector('.dashboard-page')) {
    document.addEventListener('DOMContentLoaded', initializeDashboard);
}

