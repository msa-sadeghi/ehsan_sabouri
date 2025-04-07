let countiresData = {
    Iran: ['Tehran', 'Mashhad', 'Isfahan'],
    Turkey: ['Istanbul', 'Ankara', 'Izmir'],
    USA: ['New York', 'Los Angeles', 'Chicago'],
};


let countrySelectBox = document.querySelector('.countrySelect');


countrySelectBox.addEventListener('change', function () {
    let selectedCountry = countrySelectBox.value;
    let citySelectBox = document.querySelector('.citySelect');
    citySelectBox.innerHTML = ''; // Clear previous options

    if (selectedCountry) {
        let cities = countiresData[selectedCountry];
        cities.forEach(function (city) {
            let option = document.createElement('option');
            option.value = city;
            option.textContent = city;
            citySelectBox.appendChild(option);
        });
    }
})
