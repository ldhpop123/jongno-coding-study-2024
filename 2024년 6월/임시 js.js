const api_key = 'e12b8f780a6be124be04a9b77b2383bb'

let item = document.querySelector('.item')

let country_text = document.querySelector('#country_text');
let lon_text = document.querySelector('#lon_text');
let lat_text = document.querySelector('#lat_text');

let temp_text = document.querySelector('#temp_text');
let feels_temp_text = document.querySelector('#feels_temp_text');
let max_temp_text = document.querySelector('#max_temp_text');
let min_temp_text = document.querySelector('#min_temp_text');
let pressure_text = document.querySelector('#pressure_text');
let humidity_text = document.querySelector('#humidity_text');

let wind_speed_text = document.querySelector('#wind_speed_text');
let wind_deg_text = document.querySelector('#wind_deg_text');

let sunrise_text = document.querySelector('#sunrise_text');
let sunset_text = document.querySelector('#sunset_text');

item.addEventListener('click', (e) => {
    console.log(e)
})