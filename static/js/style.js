var Invitation = function() {
	$( ".invitation-panel-tag a" ).click(function(e) {
        console.log(this.data("filter"));
    });
    var action =function() {
        var class_active = $(".invitation-panel-tag a.active").data("filter");
        $(class_active).show();
    };
    return {
        init: function(){
        	action();
        }
    }
}();

$(document).ready(function() {
    Invitation.init();
})