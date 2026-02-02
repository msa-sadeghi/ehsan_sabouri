const usersContainer = document.getElementById("usersContainer")
const loading = document.getElementById("loading")
const error = document.getElementById("error")

function showLoading(show){
    loading.style.display = show ? 'block' : 'none'
    if(show){
        usersContainer.innerHTML =  ''
        error.style.display = 'none'
    }
}

async function loadUsers() {
    showLoading(true)
    try{
        const response = await fetch("http://127.0.0.1:5000/users")
        const users = await response.json()
        displayUsers(users)
    }
    catch(error){

    }
    finally{
        showLoading(false)
    }
    
}
function displayUsers(users){
    users.forEach((u)=>{
        const userCard = document.createElement("div")
        userCard.classList.add("user-card")
        const h3 = document.createElement("h3")
        h3.innerText = u.name

        const userName = document.createElement("p")
        const nameSpan = document.createElement("span")
        nameSpan.innerText = "نام : "
        userName.innerText = u.username
        userName.prepend(nameSpan)
        userCard.append(h3,userName)
        usersContainer.append(userCard)
    })
    
}

