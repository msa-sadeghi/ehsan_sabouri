// const addAnimationButton = document.querySelector('button')
// const div = document.querySelector('div')
// const p = document.querySelector('p')
// function setAnimation(){
//     div.style.animation = 'move 4s 3'
// }
// function animationStartHandler(event){
//     p.innerHTML = "Animation started"
//     p.style.backgroundColor = 'red'
//     div.style.backgroundColor = 'red'
// }
// function animationIterationHandler(event){
//     p.innerHTML = "Animation repeated"
//     p.style.backgroundColor = 'green'
//     div.style.backgroundColor = 'green'
// }
// function animationEndHandler(event){
//     p.innerHTML = "Animation ended"
//     p.style.backgroundColor = 'blue'
//     div.style.backgroundColor = 'blue'
// }
// addAnimationButton.addEventListener('click', setAnimation)
// div.addEventListener('animationstart', animationStartHandler)
// div.addEventListener('animationiteration', animationIterationHandler)
// div.addEventListener('animationend', animationEndHandler)



const r = document.getElementById('range')
const c = document.querySelector('.container')

r.addEventListener('input', function(event){
c.style.filter = 'brightness(' + event.target.value + '%)'
})