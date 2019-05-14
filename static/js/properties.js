$(document).ready(function() {
    $('#search-btn').on( 'click', function(e){
        e.preventDefault();

        // creating variables with the input we receive through id's in index.html
        var searchText = $('#search-box').val();
        var type = $('#property-types').val();
        var status = $('#property-status').val();
        var country = $('#property_country').val();
        var city = $('#property_city').val();
        var room = $('#property-rooms').val();
        var zipcode = $('#property-zipcode').val();
        var price = Math.round($('#amount').val());
        var garden = $('#property_garden');
        var garage = $('#property_garage');
        var accessibility = $('#property_accessibility');
        var pets = $('#property_pets');
        var orderByName = $('#orderbyname');
        var orderByPrice = $('#orderbyprice')

        // creating url address with chosen search parameters
        // it will help us for the views

        console.log('price value',price)

        // creating url address with chosen search parameters
        // it will help us for the views

        var urlTail = ""

        if (type){
            urlTail += '&' + "type" + '=' + type
        }
        if (status){
            urlTail += '&' + "status" + '=' + status
        }
        if (city){
            urlTail += '&' + "city" + '=' + city
        }

        if (country){
            urlTail += '&' + "country" + '=' + country
        }

        if (room){
            urlTail += '&' + "room" + '=' + room
        }

        if (zipcode){
            urlTail += '&' + "zipcode" + '=' + zipcode
        }

        if (price){
            urlTail += '&' + "price" + '=' + price
        }

        if (garden.is(":checked")){
            urlTail += '&' + "garden" + '=' + "True"
        }

        if (garage.is(":checked")){
            urlTail += '&' + "garage" + '=' + "True"
        }

        if (accessibility.is(":checked")){
            urlTail += '&' + "accessibility" + '=' + "True"
        }

        if (pets.is(":checked")){
            urlTail += '&' + "pets" + '=' + "True"
        }
        if (orderByName.is(":checked")) {
            urlTail += '&' + "orderbyname" + '=' + "True"
        }
        if (orderByPrice.is(":checked")){
            urlTail += '&' + "orderbyprice" + '=' + "True"

        }

        queryUrl = '/properties/search/?search_filter=' + searchText + urlTail;
        console.log(queryUrl)

        $.ajax({
            url: queryUrl,
            type: 'GET',
            success: function(resp) {
                if (!$.trim(resp.data)) {
                    var newHtml = ['Sorry ',' nothing ',' matches ',' your ',' search']
                }
                else {
                console.log(resp)
                // if success show this html
                var newHtml = resp.data.map(data => {
                    return ` <div class="col-md-6 col-lg-4 mb-4">
                         <a href="/properties/${data.id}" class="prop-entry d-block">
                          <figure>
                            <img src="${data.firstImage}" alt="${data.altText}" class="img-thumbnail catalogue-image">
                          </figure>
                          <div class="prop-text">
                            <div class="inner">
                              <span class="price rounded">${ data.price }</span>
                              <h3 class="title"> ${ data.streetName } ${ data.houseNumber }</h3>
                              <p class="location">${ data.city }, ${ data.country } ${ data.zipCode }</p>
                            </div>
                            <div class="prop-more-info">
                              <div class="inner d-flex">
                                <div class="col">
                                  <span>Area:</span>
                                  <strong>${ data.size }m<sup>2</sup></strong>
                                </div>
                                <div class="col">
                                  <span>Rooms:</span>
                                  <strong>${ data.room }</strong>
                                </div>
                                <div class="col">
                                  <span>Year Built:</span>
                                  <strong>${ data.yearBuilt }</strong>
                                </div>
                                <div class="col">
                                  <span>Status:</span>
                                  <strong>${ data.status.toUpperCase() }</strong>
                                </div>
                              </div>
                            </div>
                          </div>
                        </a>
                      </div>`
                })};
                $('#properties').html(newHtml.join(''));
                //$('#search-box').val('');
            },
            error: function(xhr, status, error){
                console.error(error);
            }
        })
    })});


