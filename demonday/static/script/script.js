// Animação do botão e Collapsible do novo post.
let newPostButton = document.querySelector('.newPostButton');
let spanVertical = document.querySelector('.spanVertical');
let spanHorizontal = document.querySelector('.spanHorizontal');
let newPost = document.querySelector('.newPost');

function animacaoNewPost(){
    spanVertical.classList.toggle('verticalDesce');
    newPostButton.classList.toggle('active');
    let content = document.querySelector('.newPost');
    if (content.style.maxHeight){
        content.style.maxHeight = null;
    } else {
        content.style.maxHeight = content.scrollHeight + 'px';
    }
}

newPostButton.onclick = animacaoNewPost;


// Troca de abas do feed

function openTab(evt, tabName) {
    let i, tab, tabContent;
    tabContent = document.querySelectorAll('.tabContent');
    tab = document.querySelectorAll('.tab');
    for (i=0; i<tabContent.length; i++) {
        tabContent[i].style.display = 'none';
    }
    for (i=0; i<tab.length; i++) {
        tab[i].className = tab[i].className.replace('active', '');
    }
    document.getElementById(tabName).style.display = "flex";
    evt.currentTarget.className += " active";
}

document.querySelector('#defaultOpen').click();
