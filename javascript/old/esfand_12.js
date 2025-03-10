
let selectBox = document.getElementById('select')
console.log(selectBox)
console.log(selectBox.value)
selectBox.onchange = function(event){
    console.log(event.target.value)
}

let myInput = document.getElementById('input')
console.log(myInput.value)

myInput.value = 'something else'
let output = ''
myInput.onkeydown = function(event){
    output += event.key
    console.log(output)
}
