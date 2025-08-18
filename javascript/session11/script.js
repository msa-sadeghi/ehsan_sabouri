function dragStartHandler(event){
 event.dataTransfer.setData('my', event.target.id)
}

function dropHandler(event){
    let id = event.dataTransfer.getData('my')
    let targetElem = document.getElementById(id)

    let dropTarget = event.target
    while(!dropTarget.classList.contains('drop')){
        dropTarget = dropTarget.parent
    }
    
    dropTarget.append(targetElem)
}
function dragOverHandler(event){
    event.preventDefault()
    
}