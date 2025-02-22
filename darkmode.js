const savedTheme = localStorage.getItem('theme');
if (savedTheme === 'dark') {
    document.documentElement.setAttribute('data-theme','dark');
    themeToggle.checked = true;
} else {
    document.documentElement.setAttribute('data-theme','light');
    themeToggle.checked = false;
}
themeToggle.addEventListener('change',toggleTheme);                  
