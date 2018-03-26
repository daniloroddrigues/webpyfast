jQuery(document).ready(function ($) {

    $(window).scroll(function () {

        var scroll = $(window).scrollTop();
        console.log(scroll);

        if (scroll >= 60) {
            $('#main-nav').addClass('nav-skirt');
        } else {
            $('#main-nav').removeClass('nav-skirt');
        }
    });

});