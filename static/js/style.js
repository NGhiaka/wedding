$(document).ready(function() {
    Invitation.init();
    // CountDonw.init();
})

$(".invitation-panel-tag a").click(function() {
    Invitation.action(this);
});
var Invitation = function() {
    var construct = function() {
        var class_active = $(".invitation-panel-tag a.active").data("filter");
        $(class_active).show();
    };
    var click_tab = function(element) {
        var class_active = $(element).data("filter");
        $(".invitation-panel-content").hide();
        $(class_active).show();
    };
    var countdown = function(){
        var _year = $("#wed_countdown_datetime").data("year");
        var _month = $("#wed_countdown_datetime").data("month");
        var _day = $("#wed_countdown_datetime").data("day");
        var _hour = $("#wed_countdown_datetime").data("hour");
        var _minute = $("#wed_countdown_datetime").data("minute");
        console.log(_day);

        var countDownDate = new Date(Date.UTC(_year,_month,_day,_hour,_minute, '00')).getTime();
        console.log(countDownDate);

        var date = new Date(countDownDate);

        console.log(date.getDate());

        var x = setInterval(function() {

          // Get today's date and time
          var now = new Date().getTime();
            console.log(now);

          // Find the distance between now and the count down date
          var distance = countDownDate - now;
          // Time calculations for days, hours, minutes and seconds
          var days = Math.floor(distance / (1000 * 60 * 60 * 24));
          var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
          var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
          var seconds = Math.floor((distance % (1000 * 60)) / 1000);

          console.log(days);
          // Display the result in the element with id="demo"
          document.getElementById("wed_countdown").innerHTML = days + "d " + hours + "h "
          + minutes + "m " + seconds + "s ";

          // If the count down is finished, write some text
          if (distance < 0) {
            clearInterval(x);
            document.getElementById("wed_countdown").innerHTML = "EXPIRED";
          }
        }, 1000);
    }
    return {
        init: function() {
            construct();
            countdown();
        },
        action: function(param) {
            click_tab(param);
        }
    }
}();


var Music = function() {
    var init = function() {

    }
    return {
        init: function() {
            init();
        },
    }
}
