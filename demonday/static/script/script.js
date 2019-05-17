// Animação do botão e Collapsible do novo post.
let newPostButton = document.querySelector('.newPostButton');
let spanVertical = document.querySelector('.spanVertical');

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

// Atalhos da NavBar

let atalhoButton = document.querySelector('#atalhoButton');

function atalhosAparecem (){
    let atalhos = document.querySelector('#atalhos');
    if (atalhos.style.maxHeight){
        atalhos.style.maxHeight = null;
    } else {
        atalhos.style.maxHeight = atalhos.scrollHeight + 'px';
    }
}

atalhoButton.onclick = atalhosAparecem;


// ========================================================JOGOS
let capasPgJgs = document.querySelectorAll('aside .paginaJogos div > div');
let cntPgJgs = document.querySelectorAll('aside .paginaJogos div > div');
let sctPgJgs = document.querySelector('section .paginaJogos')


function capasJgHover(){
    let tituloPgjgs = document.querySelectorAll('aside .paginaJogos div div > div div:last-child')
    for(i=0; i<capasPgJgs.length; i++){
        sctPgJgs.style.opacity('1')
    }
}

function ALERTA(){
    alert('socorro')
}



for(i=0; i<capasPgJgs.length; i++){
    capasPgJgs[i].onclick = capasJgHover();
}