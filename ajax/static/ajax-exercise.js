"use strict";


// PART 1: SHOW A FORTUNE

function showFortune(evt) {
      console.log('this is the event')
      console.log(evt)
    $.get('/fortune', {}, (res) => {
      console.log('this is the response')
      console.log(res)
      $('#fortune-text').html(res);
    });

}

$('#get-fortune-button').on('click', showFortune);





// PART 2: SHOW WEATHER

function showWeather(evt) {
    evt.preventDefault();

    let url = "/weather.json";
    let formData = {"zipcode": $("#zipcode-field").val()};
    $.get(url, formData, (res) => {
      $('#weather-info').html(res.forecast)
    })

    // TODO: request weather with that URL and show the forecast in #weather-info
}

$("#weather-form").on('submit', showWeather);




// PART 3: ORDER MELONS

function orderMelons(evt) {
    evt.preventDefault();

    // TODO: show the result message after your form
    const formInputs = {
      'qty': $('#qty-field').val(),
      'melon_type': $('#melon-type-field').val()
    };
    $.post('/order-melons.json', formInputs, (res) => {
      console.log(res)
      if(res.code === 'ERROR') {
        let full_res = res.code + ': ' + res.msg;
        $('#order-status').html(full_res).addClass("order-error")}
      else {
        let full_res = res.code + ': ' + res.msg;
      $('#order-status').html(full_res)
      }
    });
    // TODO: if the result code is ERROR, make it show up in red (see our CSS!)
}

$("#order-form").on('submit', orderMelons);


