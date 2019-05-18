let nomeSite = document.querySelector('#nomeSite');
let path = window.location.pathname;

if (path == '/'){
    nomeSite.style.display = 'none';
} else {
    nomeSite.style.display = 'flex';
}