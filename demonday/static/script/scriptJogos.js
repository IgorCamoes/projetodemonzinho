let capasPgJgs = document.querySelectorAll('aside .paginaJogos div > div');
let cntPgJgs = document.querySelectorAll('aside .paginaJogos div > div');
let sctPgJgs = document.querySelector('section > .paginaJogos')
let i;

function apareceSection(){
    for(i=0; i<capasPgJgs.length; i++){
        capasPgJgs[i].addEventListener("click", function() {
            sctPgJgs.style.opacity("1");
          });
        }
    }