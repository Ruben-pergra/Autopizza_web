document.addEventListener('DOMContentLoaded', () => {
    const loginBtn = document.getElementById('login-btn');
    const loginModal = document.getElementById('login-modal');
    const closeModal = document.getElementById('close-modal');
    const loginForm = document.getElementById('login-form');
    const userDisplay = document.getElementById('user-display');
    const userContainer = document.getElementById('user-container');
    const logoutOption = document.getElementById('logout-option');
    const logoutBtn = document.getElementById('logout-btn');
  
    const savedUsername = localStorage.getItem('username');
    if (savedUsername) {
      loginBtn.classList.add('hidden');
      userDisplay.textContent = savedUsername;
      userContainer.classList.remove('hidden');
    }
  
    loginBtn?.addEventListener('click', () => {
      loginModal.classList.remove('hidden');
    });
  
    closeModal?.addEventListener('click', () => {
      loginModal.classList.add('hidden');
    });
  
    loginForm?.addEventListener('submit', (e) => {
      e.preventDefault();
      const username = document.getElementById('username').value;
      localStorage.setItem('username', username);
      loginModal.classList.add('hidden');
      loginBtn.classList.add('hidden');
      userDisplay.textContent = username;
      userContainer.classList.remove('hidden');
    });
  
    userDisplay?.addEventListener('click', () => {
      logoutOption.classList.toggle('hidden');
    });
  
    logoutBtn?.addEventListener('click', () => {
      localStorage.removeItem('username');
      location.reload();
    });
  
    document.addEventListener('click', (e) => {
      if (!userContainer.contains(e.target)) {
        logoutOption.classList.add('hidden');
      }
    });
});

  // Funcionalidad para el menú desplegable
const menuToggle = document.getElementById('menu-toggle');
const menuDropdown = document.getElementById('menu-dropdown');

menuToggle?.addEventListener('click', (e) => {
  e.stopPropagation(); // evita que el evento burbujee
  menuDropdown.classList.toggle('hidden');
});

// Cierra el menú si se hace clic fuera
document.addEventListener('click', (e) => {
  if (!menuDropdown.contains(e.target) && !menuToggle.contains(e.target)) {
    menuDropdown.classList.add('hidden');
  }
});
