let inputs = document.getElementsByTagName('input')
let form = document.getElementsByClassName('form')[0]

function usernameFocus(){
    inputs[0].style.border = "1px solid blue"
}
function usernameBlur(){
    let username = inputs[0].value
    let span1 = document.getElementById('span1')
    if (username.length < 8){
        span1.style.display = 'inline'
        inputs[0].style.border = "1px solid red"
        span1.innerText = 'طول نام کاربری باید حداقل هشت باشد'
    } else{
        span1.style.display = 'none'
        inputs[0].style.border = 0
    }
    
}
function passwordFocus(){
    console.log('Focus username')
}
function passwordBlur(){
    console.log('blur username')
}

