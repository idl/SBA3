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

	// Regiser Admin User
	// Hide select school dropdown when click Global Admin checkbox and set to ''
	// If a school is selected while Global Admin checkbox is asserted, uncheck it
	$('#id_superuser').change(function() {
		var originalOptionsHTML = $('#id_school').html();
		// console.log("Initial val: '" + $('#id_school').val() + "'");
		// console.log("'" + typeof $('#id_superuser:checked').val() + "'")
		if($(this).is(':checked')) {
			console.log('CHECKED');
			$('.school-select').fadeOut();
		} else {
			$('.school-select').fadeIn();
		}
	});
})(jQuery);