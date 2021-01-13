$(function () {

    $('.carousel').carousel({
        pause: ""
    });

     var mySwiper = new Swiper ('.swiper-container');
     var mySwiper = new Swiper ('.many_products_swiper', {
        scrollbar: {
            el: '.swiper-scrollbar',
          }
     });



     $(".home").innerHeight($(".home .carousel").innerHeight());

     $(window).on("resize", function () {

        $(".home").innerHeight($(".home .carousel").innerHeight());

     });

     $(window).on("scroll", function () {

        if ($(this).scrollTop() >= 20) {

            $("header.main_header .logo img").attr("src", "imgs/global/logo_black.png");

            $("header.main_header").addClass("active_bg");

        } else {

            $("header.main_header .logo img").attr("src", "imgs/global/logo_white.png");

            $("header.main_header").removeClass("active_bg");

        }

     });

    $("header.main_header .menu .toggle_menu button").on("click", function () {

        $(this).toggleClass("active");

        $("aside.aside_menu").toggleClass("active");

        $("nav.small_menu").toggleClass("active");

    });

    $("aside.aside_menu .aside_head .btn-close").on("click", function () {

        $(this).parents("aside.aside_menu").toggleClass("active");

        $("header.main_header .menu .toggle_menu button").toggleClass("active");

    });

    $(".btn_close_menu").on("click", function () {

        $("nav.small_menu").toggleClass("active");

        $("header.main_header .menu .toggle_menu button").toggleClass("active");

    });

    $(".front_part").innerHeight($(".back_part").innerHeight());

    $(".our_skills .our_skills_tab li").on("click", function () {

        $(this).addClass("active").siblings().removeClass("active");

        $("#" + $(this).data("tab")).addClass("tab_show").parents(".col-12").siblings().find(".tab_removeclass").removeClass("tab_show");

    });

    var countDownDate = new Date("August 29, 2019 00:00:00").getTime();

    var runCount = setInterval(function () {

        var now = new Date().getTime(),

            distance = countDownDate - now,

            days = Math.floor(distance / (1000 * 60 * 60 * 24)),

            hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)),

            minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60)),

            seconds = Math.floor((distance % (1000 * 60)) / 1000);


        $(".time_area_1").html(days + "<div>days</div>");
        $(".time_area_2").html(hours + "<div>hours</div>");
        $(".time_area_3").html(minutes + "<div>minutes</div>");
        $(".time_area_4").html(seconds + "<div>seconds</div>");

        if (distance < 0) {
            clearInterval(runCount);
        }

    }, 1000);

});