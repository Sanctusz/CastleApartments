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
        show('confirm_step','cc_step','ci_step','confirm_li','confirm_a');
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