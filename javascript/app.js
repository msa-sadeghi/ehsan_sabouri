let button = document.querySelector("button")
let div = document.querySelector("div")


div.addEventListener('click',  function(){
    console.log("div clicked")
},{capture:true})
button.addEventListener('click',  function(){
    console.log("button clicked")
})