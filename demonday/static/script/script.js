let divCadastro = document.querySelector('article div > div:first-child');
let divLogin = document.querySelector('article div > div:last-child');
let botaoCadastro = document.querySelector('.cadastro input:nth-child(3)');
let botaoLogin = document.querySelector('.login input:nth-child(3)');
let newPostButton = document.querySelector('.newPostButton');
let spanVertical = document.querySelector('.spanVertical');
let spanHorizontal = document.querySelector('.spanHorizontal');
let newPost = document.querySelector('.newPost')

function ligarDiv(){
    divCadastro.classList.toggle('ligou');
    divLogin.classList.toggle('ligou');
}

function animacaoNewPost(){
    spanVertical.classList.toggle('verticalDesce');
    newPost.classList.toggle('activeNewPost');
}

botaoCadastro.onclick = ligarDiv();
botaoLogin.onclick = ligarDiv();

newPostButton.onclick = animacaoNewPost;
