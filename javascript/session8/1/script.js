const contextMenu = document.getElementById("contextMenu")

function myFunction(event){
    event.preventDefault()
    if(contextMenu.style.display === 'none'){
        contextMenu.style.display = 'block'
    }
}
document.addEventListener("contextmenu", myFunction)
