let newPostButton = document.querySelector('.newPostButton');
let spanVertical = document.querySelector('.spanVertical');
let spanHorizontal = document.querySelector('.spanHorizontal');
let newPost = document.querySelector('.newPost');

function animacaoNewPost(){
    spanVertical.classList.toggle('verticalDesce');
    newPost.classList.toggle('activeNewPost');
}

newPostButton.onclick = animacaoNewPost;