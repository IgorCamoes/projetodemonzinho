// Animação do botão e Collapsible do novo post.

if(path == '/feed/'){
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

//Collapsible posts do feed

let postButton = document.querySelectorAll('.postButton');
let spanVertical1 = document.querySelectorAll('.spanVertical1');
let postsConteudo = document.querySelectorAll('.postsConteudo');
let p = 0;

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


  let divPost = document.querySelectorAll('.postsTitulo');
  let divConteudo = document.querySelectorAll('.postsTitulo');
  let i;

  for (i = 0; i < divPost.length; i++) {
    divPost[i].addEventListener("click", function() {
      this.classList.toggle("postAtivo");
      let content = divConteudo.nextElementSibling;
      if (content.style.maxHeight){
        content.style.maxHeight = null;
      } else {
        content.style.maxHeight = content.scrollHeight + "px";
      } 
    });
  }
}