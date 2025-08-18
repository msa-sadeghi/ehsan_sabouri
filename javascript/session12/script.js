function insertName(){
    localStorage.setItem('name',  'sara')
}

function getName(){
    let localName = localStorage.getItem('name')
    console.log(localName)
}

function clearData(){
    localStorage.clear()
}