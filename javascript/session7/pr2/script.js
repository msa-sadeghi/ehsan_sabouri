const inputElem = document.querySelector('input')
const todosElem = document.querySelector('.todos')
const formElem = document.querySelector('form')

function addNewTodo(val){
    let newLi = document.createElement("li")
    newLi.className = "list-group-item d-flex justify-content-between align-items-center"
    let span = document.createElement("span")
    let deleteElem = document.createElement("i")
    deleteElem.className = "fa fa-trash"
    deleteElem.addEventListener('click', function(event){
        event.target.parentElement.remove()
    })
    span.innerHTML = val;
    newLi.append(span, deleteElem)
    todosElem.append(newLi)
}

formElem.addEventListener('submit', function(event){
    event.preventDefault()
})

inputElem.addEventListener('keydown', function(event){
    let val = event.target.value
    if(event.key == 'Enter'){
        inputElem.value = ''
        addNewTodo(val)
    }
})