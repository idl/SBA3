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
	$('#id_register_admin_superuser').change(function() {
		// .stop() - http://stackoverflow.com/questions/2857998/stop-jquery-animations-stacking
		if($(this).is(':checked')) {
			$('.school-select').stop().fadeOut(function() {
				$('.form-note').stop().fadeIn();
			});
		} else {
			$('.form-note').stop().fadeOut(function() {
				$('.school-select').stop().fadeIn();
			});
		}
	});
	$('#id_register_admin_school').change(function() {
		// hiding the superadmin checkbox causes submit button to shift up
		if($(this).val() != '') {
			var superuserselect_height = $('.superuser-select').height();
			$('.superuser-select').stop().fadeOut(function() {
				$('.registerAdminUserForm button[type="submit"]').css('margin-top', superuserselect_height - 3);
			});
		} else {
			$('.superuser-select').stop().fadeIn();
			$('.registerAdminUserForm button[type="submit"]').css('margin-top', 0);
		}
	});

	$('.editAdmin').click(function() {
		var user_row, user_id, user_email, user_school_id, user_school_name;
		user_row = $(this).parent().parent();
		user_id = user_row.attr('data-user-id');
		user_email = user_row.find('.user_email').html();
		user_school_id = user_row.attr('data-school-id');
		user_school_name = user_row.find('.user_school_name').html();

		$('.modal .modal-title small').html(user_row.find('.user_email').html());
		$('.editGlobalAdminUser form, .editSchoolAdminUser form').attr('action', '/admin/updateadmin/'+user_id);
		// is global admin
		if(user_school_name === undefined) {
			$('#id_edit_globaladmin_email').val(user_email);
		} else { // is school admin
			$('#id_edit_schooladmin_email').val(user_email);
			$('#id_edit_schooladmin_school').val(user_school_id);
		}
	});
	$('.deleteAdmin').click(function() {
		var user_row, user_id, user_email;
		user_row = $(this).parent().parent();
		user_id = user_row.attr('data-user-id');
		user_email = user_row.find('.user_email').html();
		$('.deleteAdminUser form').attr('action', '/admin/deleteadmin/'+user_id);
		$('.modal .modal-title small').html(user_row.find('.user_email').html());
	});
	$('.editGlobalAdminUser .change-password input').change(function() {
		if($(this).is(':checked')) {
			$('.change-password-section').slideToggle();
		} else {
			$('.change-password-section').slideToggle();
		}
	});
	$('.editSchoolAdminUser .change-password input').change(function() {
		if($(this).is(':checked')) {
			$('.change-password-section').slideToggle();
		} else {
			$('.change-password-section').slideToggle();
		}
	});
	$('.deleteSchool').click(function() {
		var school_row, school_id;
		school_id = $(this).attr('data-school-id');
		console.log(school_id);
		$('.deleteSchool form').attr('action', '/admin/deleteschool/'+school_id);
		$('.modal .modal-title small').html($(this).attr('data-school-name'));
	});
})(jQuery);