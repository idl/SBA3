(function($, undefined) {
	"use strict";

	// Javascript to enable link to tab
	var hash = document.location.hash;
	var prefix = "";
	if (hash) {
	    $('.nav-pills a[href='+hash.replace(prefix,"")+']').tab('show');
	}

	// Change hash for page-reload
	$('.nav-pills a').on('shown', function (e) {
	    window.location.hash = e.target.hash.replace("#", "#" + prefix);
	});
})(jQuery);