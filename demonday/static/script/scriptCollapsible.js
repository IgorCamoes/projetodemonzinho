//Collapsible posts do feed

let postButton = document.querySelectorAll('.postButton');
let spanVertical1 = document.querySelectorAll('.spanVertical1');
let postsConteudo = document.querySelectorAll('.postsConteudo');
let p;

function abrirPost(){
  for(p=0; p<postButton.length; p++){
      spanVertical1[p].classList.toggle('verticalDesce1');
      postButton[p].classList.toggle('active1');
      if (postsConteudo[p].style.maxHeight){
          postsConteudo[p].style.maxHeight = null;
      } else {
          postsConteudo[p].style.maxHeight = postsConteudo[p].scrollHeight + 'px';
      }
  }
}
postButton[p].onclick = abrirPost;
