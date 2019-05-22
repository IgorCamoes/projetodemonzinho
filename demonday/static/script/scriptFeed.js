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


let navTabArea = document.querySelector('#navTabArea');
let navBar = document.querySelector('nav');

// Deixar a nav das abas sempre grudando na Nav:

if (navBar.style.height != '7vh'){
    navTabArea.style.top = '44px';
}

// let divPost = document.querySelectorAll('.postsTitulo');
// let divConteudo = document.querySelectorAll('.postsTitulo');
// let j;

// for (j = 0; j < divPost.length; j++) {
//   divPost[j].addEventListener("click", function() {
//     this.classList.toggle("postAtivo");
//     let content1 = divConteudo.nextElementSibling;
//     if (content1.style.maxHeight){
//       content1.style.maxHeight = null;
//     } else {
//       content1.style.maxHeight = content1.scrollHeight + "px";
//     } 
//   });
// }
