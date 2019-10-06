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
        countdown(class_active);
        $("."+class_active).show();
    };
    var click_tab = function(element) {
        var class_active = $(element).data("filter");
        $(".invitation-panel-tag a").removeClass('active');
        $(element).addClass('active');

        $(".invitation-panel-content").hide();
        $("."+class_active).show();
        countdown(class_active);

    };
    var countdown = function(id) {
        var _datetime = $("#wed_countdown_"+id).data("datetime");
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

            $("#wed_countdown_"+id).html(_htmltag);
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
            
        },
        action: function(param) {
            click_tab(param);
        }
    }
}();


var infinite = new Waypoint.Infinite({
    element: $('.infinite-container')[0],
    onBeforePageLoad: function () {
        $('.infinite-container').addClass('fade-up-active');

        $('.loading').show();
    },
    onAfterPageLoad: function (items) {
        var strhtml = '';
        $.each( items, function( key, value ) {
            if (key%2==0){
                strhtml = 
                `<div data-animation="animation_blocks" data-bottom="@class:noactive" data--10-bottom="@class:active">  
                    <div class="row wed_story_row">` + value + 
                        `<div class="col-md-2 hidden-sm hidden-xs text-center">   
                            <div class="wed_story_center">
                                <div class="wed_story_content">
                                    <div class="wed_heart_container">
                                        <img class="wed_heart_1" src="'../images/small_people/heart_3.png'%}" alt="">
                                        <img class="wed_heart_2" src="'../images/small_people/heart_2.png'%}" alt="">
                                    </div>
                                    <div class="wed_story_small_img">
                                        <img src="'../images/small_people/couple_1.png'%}" alt="">
                                    </div>

                                </div>
                            </div>
                        </div>`;
            }
            else{
                strhtml += value + '<div class="wed_vertical_line wed_line_top hidden-sm hidden-xs"></div></div></div>';
                $(this).appendChild(strhtml);
                strhtml = '';
            }
                        
                    

            console.log( key  );
            console.log( value  );
        });
        $('.loading').hide();
    },
    
});


var Music = function() {
    var init = function() {

    }
    return {
        init: function() {
            init();
        },
    }
}