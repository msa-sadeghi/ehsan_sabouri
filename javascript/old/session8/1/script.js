const contextMenu = document.getElementById("contextMenu")

function myFunction(event){
    event.preventDefault()
    if(contextMenu.style.display === 'none'){
        contextMenu.style.display = 'block'
        contextMenu.style.left = event.pageX + 'px'
        contextMenu.style.top = event.pageX + 'px'
    } else{
        contextMenu.style.left = event.pageX + 'px'
        contextMenu.style.top = event.pageX + 'px'
    }
}

function myFunction2(){
    contextMenu.style.display = 'none'
}
document.body.addEventListener("contextmenu", myFunction)
document.body.addEventListener("click", myFunction2)
