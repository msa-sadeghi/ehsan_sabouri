const nameInput = document.getElementById('name');
const button = document.querySelector('button');
const nameError = document.getElementById('nameError');
const info = document.getElementById('info');

button.addEventListener('click', (e) => {
    e.preventDefault()
    const name = nameInput.value.trim();
    let emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if(!emailPattern.test(name)) {
        nameError.style.display = 'block';
        nameError.textContent = 'نام باید حداقل ۳ کاراکتر باشد.';
    }else{
        nameError.style.display = 'none';
    }

    let newDiv = document.createElement('div')
    newDiv.innerHTML = `<h1>اسم:</h1>
    
    `

    info.append(newDiv)
    info.style.display = "block"


})