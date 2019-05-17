$(document).ready(function () {
        var price1 = $('#price1').text();
        price1 = price1.replace(/\D/g,'');
        price1 = parseInt(price1);
        $('#currency').on('change', function (e) {
            e.preventDefault();

            var currency_type = $('#currency').val();
            var currency_value;

            queryUrl = 'http://apis.is/currency/lb';
            console.log(queryUrl)
            $.ajax({
                'url': queryUrl,
                'type': 'GET',
                'dataType': 'json',
                'success': function (response) {
                    if (currency_type === 'ISK'){
                        currency_value = price1
                    }
                    if (currency_type === 'EUR'){
                        currency_value = price1 / response.results[0].askValue
                    }
                    else if (currency_type === 'USD'){
                        currency_value = price1 / response.results[1].askValue
                    }
                    else if (currency_type === 'GBP'){
                        currency_value = price1 / response.results[2].askValue
                    }
                    else if (currency_type === 'JPY'){
                        currency_value = price1 / response.results[3].askValue
                    }
                    else if (currency_type === 'NOK'){
                        currency_value = price1 / response.results[4].askValue
                    }
                    var newHtml = [Math.round(currency_value).toString().replace(/(\d)(?=(\d{3})+(?!\d))/g, '$1,'), ' '+currency_type]
                    $('#price1').html(newHtml.join(''));
                    $('#price2').html(newHtml.join(''));
                }
            });
        })
});