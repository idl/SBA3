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
		if($(this).is(':checked')) {
			$('.school-select').fadeOut(function() {
				$('.form-note').fadeIn();
			});
		} else {
			$('.form-note').fadeOut(function() {
				$('.school-select').fadeIn();
			});
		}
	});
	$('#id_school').change(function() {
		if($(this).val() != '') {
			$('.superuser-select').fadeOut();
		} else {
			$('.superuser-select').fadeIn();
		}
	});

	$('.editAdmin').click(function() {
		var user_id = $(this).parent().parent().attr('data-user-id');
	});
})(jQuery);