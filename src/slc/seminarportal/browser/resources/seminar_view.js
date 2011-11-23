var jq = jQuery.noConflict();
jq(document).ready(function(){
    jq("div.big-target a").bigTarget({
        clickZone : 'div:eq(0)' // jQuery parent selector
    });
});

var SEMINAR = {}

SEMINAR.loadSpeakerDetails = function () {
    jQuery.fancybox.showActivity();
    jQuery.ajax({
        async: false,
        type: 'GET',
        url: this.href,
        success: function(data) {
            jQuery("#speaker-overlay #content")
                .replaceWith(jQuery(data)
                             .find("#content"));
        }
    });
};

jQuery(document).ready(function() {
    if (jQuery("a.speaker-fancybox").length>0) {
        jQuery("a.speaker-fancybox").fancybox({
            'transitionIn'   : 'elastic',
            'transitionOut'  : 'elastic',
            'titlePosition'  : 'over',
            'overlayOpacity' : 0.7,
            'overlayColor'   : '#FFF',
            'showNavArrows'  : false,
            'onStart'        : SEMINAR.loadSpeakerDetails,
            'content'        : jQuery('#speaker-overlay'),
        });
    }
})
