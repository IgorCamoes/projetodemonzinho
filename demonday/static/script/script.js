let divCadastro = document.querySelector('article div > div:first-child');
let divLogin = document.querySelector('article div > div:last-child');
let botaoCadastro = document.querySelector('.cadastro input:nth-child(3)');
let botaoLogin = document.querySelector('.login input:nth-child(3)');

function ligarDiv(){
    divCadastro.classList.toggle('ligou');
    divLogin.classList.toggle('ligou');
}

botaoCadastro.onclick = ligarDiv();
botaoLogin.onclick = ligarDiv();