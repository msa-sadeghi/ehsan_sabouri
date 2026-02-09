async function getWeather(city) {
    try{
        const response = await fetch(`http://127.0.0.1:5000/city/${city}`)
        const data = await response.json()
        renderItems(data)
    }
    catch(error){
        console.log(error)
    }
}
const weatherContainer = document.getElementById("weatherContainer")
function renderItems(item){
    weatherContainer.innerHTML =  ""
    const cardItem =  document.createElement("div")
    const h3 = document.createElement("h3")
    h3.innerText = item.name
    const tempSpan = document.createElement("span")
    tempSpan.innerText = "دما:"
    const tempElement = document.createElement("span")
    tempElement.innerHTML = item.icon
    cardItem.append(h3,tempSpan, tempElement)
    weatherContainer.append(cardItem)    
   
}


function searchWeather(){
    let cityInputValue = document.getElementById("cityInput")
    getWeather(cityInputValue)
}