$(document).ready(function () {
    $('#ci_a').on('click', function (e) {
        e.preventDefault();
        show('ci_step','cc_step','confirm_step');
    });

    $('#cc_a').on('click', function (e) {
        e.preventDefault();
        show('cc_step','ci_step','confirm_step');
    });

    $('#confirm_a').on('click', function (e) {
        e.preventDefault();
        show('confirm_step','ci_step','cc_step');
    });

    $('#cc_next').on('click', function (e) {
        e.preventDefault();
        show('cc_step','ci_step','confirm_step', 'cc_li', 'cc_a');

    });

    $('#confirm_next').on('click', function (e) {
        e.preventDefault();
        var fname = $('#id_fname').val();
        var mname = $('#id_mname').val();
        var lname = $('#id_lname').val();
        var ssn = $('#id_ssn').val();
        var streetname = $('#id_streetName').val();
        var housenumber = $('#id_houseNumber').val();
        var zipcode = $('#id_zipCode').val();
        var city = $('#id_city').val();
        var country = $('#id_country').val();
        var ccname = $('#id_ccName').val();
        var ccnumber = $('#id_ccNumber').val();
        var cvc = $('#id_CVC').val();
        var expirationdate = $('#id_expirationDate').val();
        show('confirm_step','cc_step','ci_step','confirm_li','confirm_a');
        document.getElementById("fname").innerHTML = fname;
        document.getElementById("mname").innerHTML = mname;
        document.getElementById("lname").innerHTML = lname;
        document.getElementById("SSN").innerHTML = ssn;
        document.getElementById("streetName").innerHTML = streetname;
        document.getElementById("houseNumber").innerHTML = housenumber;
        document.getElementById("zipCode").innerHTML = zipcode;
        document.getElementById("city").innerHTML = city;
        document.getElementById("country").innerHTML = country;
        document.getElementById("ccName").innerHTML = ccname;
        document.getElementById("ccNumber").innerHTML = ccnumber;
        document.getElementById("CVC").innerHTML = cvc;
        document.getElementById("expirationDate").innerHTML = expirationdate;
    });
});

function show(shown, hidden, hidden2, completed_li, completed_a) {
    document.getElementById(shown).style.display = 'block';
    document.getElementById(hidden).style.display = 'none';
    document.getElementById(hidden2).style.display = 'none';
    if (completed_li) {
        document.getElementById(completed_li).className += ' bc_complete';
    }
    if (completed_a === 'cc_a') {
        var anchor = document.getElementById(completed_a);
        anchor.setAttribute('href','#');
    }
    if (completed_a === 'confirm_a') {
        var anchor = document.getElementById(completed_a);
        anchor.setAttribute('href','#');
    }
    return false;
}