$(document).ready(function() {
    Invitation.init();
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
    return {
        init: function() {
            construct();
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