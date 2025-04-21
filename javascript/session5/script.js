let usernameInput = document.querySelector(".username");
let passwordInput = document.querySelector(".password");

let userNameMessage = document.querySelector(".username-validation");
let passwordMessage = document.querySelector(".password-validation");
function usernameValidation(){
    if (usernameInput.value.length < 12){
        userNameMessage.innerHTML = "Username must be at least 12 characters long";
        userNameMessage.style.color = "red";
        userNameMessage.style.display = "block";
    }
    else{
        userNameMessage.innerHTML = "Valid Username";
        userNameMessage.style.color = "green";
        userNameMessage.style.display = "block";
    }
}

// function dblclickEvent(){
//     console.log("double clicked on the button");
// }

// let titleH1 = document.querySelector("h1"); 
// titleH1.addEventListener("click", function(){ 
//     console.log("clicked on the title");
//     titleH1.style.color = "red";
// } )
// console.log(document.body)
// let colors = ['red', 'yellow', 'blue', 'green', 'purple', 'orange'];
// let index = 0;
// setInterval(function(){
//     console.log("changing color");
//     document.body.style.backgroundColor = colors[index];
//     index++;
//     if (index >= colors.length){
//         index = 0;
//     }
// }, 2000);

// let countriesElem = document.querySelector("#countries");
// let countyNameElem = document.querySelector(".countyName");
// let descriptionsElem = document.querySelector(".descriptions");
// let countryImageElem = document.querySelector(".container img");
// console.log(countryImageElem)
// let descriptions = {
//     "Usa": "The United States of America is a country primarily located in North America.",
//     "Canada": "Canada is a country in North America.",
//     "Mexico": "Mexico is a country in the southern portion of North America.",
//     "UK": "The United Kingdom is a country located off the northwestern coast of the European mainland.",
//     "Germany": "Germany is a country in Central and Western Europe.",
//     "France": "France is a country whose territory consists of metropolitan France in Western Europe and several overseas regions and territories."
// }
// function countryChange(){
//     countyNameElem.innerHTML =countriesElem.value;
//     descriptionsElem.innerHTML = descriptions[countriesElem.value.toString()];
//     descriptionsElem.style.color = "blue";
//     countryImageElem.src = `../usa.png`;
// }