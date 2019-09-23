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
    var countdown = function() {
        var _datetime = $("#wed_countdown_datetime").data("datetime");
        
        var countDownDate = new Date(_datetime).getTime()

        var date = new Date(countDownDate);
        var x = setInterval(function() {

            // Get today's date and time
            var now = new Date().getTime();

            // Find the distance between now and the count down date
            var distance = countDownDate - now;
            // Time calculations for days, hours, minutes and seconds
            var days = Math.floor(distance / (1000 * 60 * 60 * 24));
            var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            var seconds = Math.floor((distance % (1000 * 60)) / 1000);

            // Display the result in the element with id="demo"
            var _htmltag = 
            `<span class="countdown-row countdown-show4">
                <span class="countdown-section">
                    <span class="countdown-amount">`+ days +`</span>
                    <span class="countdown-period">Days</span>
                </span>
                <span class="countdown-section">
                    <span class="countdown-amount">`+ hours +`</span>
                    <span class="countdown-period">Hours</span>
                    </span>
                <span class="countdown-section">
                    <span class="countdown-amount">`+ minutes +`</span>
                    <span class="countdown-period">Minutes</span>
                </span>
                <span class="countdown-section">
                    <span class="countdown-amount">`+ seconds +`</span>
                    <span class="countdown-period">Seconds</span>
                </span>
            </span>`;

            $("#wed_countdown_datetime").html(_htmltag);
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