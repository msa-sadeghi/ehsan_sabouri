const container = document.getElementById("usersContainer")
const loadingDev = document.getElementById("loading")
const errorDiv = document.getElementById("error")

function showLoading(show = true){
    loadingDev.style.display = show ? 'block' : 'none'

}

function showError(message){
    errorDiv.style.display = "block"
    errorDiv.textContent = message
}

async function loadUsers() {
    showLoading(true)
    try{
        const response = await fetch("https://jsonplaceholder.typicode.com/users")
        if(!response.ok){
            throw new Error("error")
        }
        const users = await response.json()
        displayUsers(users)
    }catch(error){
        showError(error.message)
    }finally{
        showLoading(false)
    }
}
function displayUsers(users){
    users.map(user=>{
        const userCard = document.createElement("div")
        userCard.classList.add("user-card")
        const h3 = document.createElement("h3")
        h3.textContent = user.name
        const userName = document.createElement("p")
        userName.textContent = user.username
        userCard.append(h3, userName)
        container.append(userCard)
    })
}