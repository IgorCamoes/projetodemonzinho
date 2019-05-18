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
