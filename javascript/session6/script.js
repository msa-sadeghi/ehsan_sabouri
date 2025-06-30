
const countrySelectBox = document.querySelector(".countrySelect")
const citySelectBox = document.querySelector(".citySelect")
let countriesData = {
    Iran: ['Tehran', 'Isfahan', 'Shiraz'],
    Turkey: ['Istanbul', 'Ankara', 'Izmir'],
    USA: ['New York', 'Los Angeles', 'Chicago'],
}

countrySelectBox.addEventListener("change", function () {
    if (countrySelectBox.value === "Please Select") {
        citySelectBox.innerHTML = "";
        citySelectBox.innerHTML += "<option>Select City</option>";
      } else {
        let mainCountryName = countrySelectBox.value; // Us
        let mainCountryCities = countriesData[mainCountryName];
    
        citySelectBox.innerHTML = "";
    
        mainCountryCities.forEach(function (city) {
            citySelectBox.innerHTML += "<option>" + city + "</option>";
        });
      }
})