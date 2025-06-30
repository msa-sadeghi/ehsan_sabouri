const togglepassword = document.getElementsByClassName('toggle-password')[0];
const inputElement = document.getElementById('password-field');
togglepassword.addEventListener('click', function(){
    if(inputElement.type == 'text'){
        inputElement.type = "password"
        togglepassword.classList.add('active')
    }else{
        
        inputElement.type = "text"
        togglepassword.classList.remove('active')
    }
})