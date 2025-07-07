const inputFieldElement = document.querySelector("#input-field")
const colorBoxes = document.querySelectorAll('.color-box')
const btnSave = document.querySelectorAll('#btn-save')
const btnDelete = document.querySelectorAll('#btn-delete')
const listedElement = document.querySelector('#listed')

colorBoxes.forEach(function(btn){
    btn.addEventListener("click", function(e){
        let c = e.target.style.backgroundColor
        inputFieldElement.style.backgroundColor = c

    })
})