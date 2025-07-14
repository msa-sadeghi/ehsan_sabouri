const inputFieldElement = document.querySelector("#input-field")
const colorBoxes = document.querySelectorAll('.color-box')
const btnSave = document.querySelector('#btn-save')
const btnDelete = document.querySelector('#btn-delete')
const listedElement = document.querySelector('#listed')

colorBoxes.forEach(function(btn){
    btn.addEventListener("click", function(e){
        let c = e.target.style.backgroundColor
        inputFieldElement.style.backgroundColor = c

    })
})

function generateNewNote(){
    let newDiv = document.createElement('div')
    newDiv.style.backgroundColor = inputFieldElement.style.backgroundColor;
    newDiv.className = "card"
    let newNoteP = document.createElement('p')
    newNoteP.innerHTML = inputFieldElement.value
    newNoteP.className = 'card-text p-3'
    newDiv.append(newNoteP)

    listedElement.append(newDiv)

}

btnSave.addEventListener('click', generateNewNote)