$(document).ready(function() {
    $('#search-btn').on( 'click', function(e){
        e.preventDefault();

        var searchText = $('#search-box').val();
        var type = $('#property-types').val();
        var status = $('#property-status').val();
        var location = $('#property_country').val();
        var rooms = $('#property-rooms').val();
        // var size = $('#amount').val();


        var urlTail = ""

        if (type){
            urlTail += '&' + "type" + '=' + type
        }
        if (status){
            urlTail += '&' + "status" + '=' + status
        }
        if (location){
            urlTail += '&' + "location" + '=' + location
        }

        if (rooms){
            urlTail += '&' + "rooms" + '=' + rooms
        }

        // if (size)(
        //     urlTail += '&' + "size" + '=' + size
        // )

        $.ajax({
            url: '/properties/search/?search_filter=' + searchText + urlTail,
            type: 'GET',
            success: function(resp) {
                console.log(resp)
                var newHtml = resp.data.map(data => {
                    return ` <div class="col-md-6 col-lg-4 mb-4">
                         <a href="property-details.html" class="prop-entry d-block">
                          <figure>
                            <img src="${data.firstImage}" alt="Image" class="img-fluid">
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
                                  <strong>${ data.status }</strong>
                                </div>
                              </div>
                            </div>
                          </div>
                        </a>
                      </div>`
                });
                $('#properties').html(newHtml.join(''));
                //$('#search-box').val('');

            },
            error: function(xhr, status, error){
                // TODO show toestr
                console.error(error);
            }
        })
    });
});


// var houseType = $('#property-types').val();
// var propertyStatus = $('#property-status').val();
// var location = $('#property_country').val();
// var rooms = $('#property-rooms').val();
// var size = $('#amount').val();