let capasPgJgs = document.querySelector('aside .paginaJogos div div div:first-child img');
// let cntPgJgs = document.querySelector('aside .paginaJogos div > div');
let sctPgJgs = document.querySelector('section .paginaJogos');
let q;

function apareceSection(){
  // for(q=0; q<capasPgJgs.length; q++){
    sctPgJgs.classList.toggle('active2');
  }
// }
capasPgJgs.onclick = apareceSection;

