  $('document').ready(function() {
    $('#classification').on('change', function() {
        console.log('#classification loaded');
      if($(this).val() == 'master' || $(this).val() == 'doctorate') {
        $('.ifNotGrad').css('background', 'red'); //.hide();
      } else {
        $('.ifNotGrad').css('background', 'white'); //.show();
      }
    });
    $('#isDistance').on('change', function() {
      if($(this).val() == 'yes') {
        $('.ifDistance').css('background', 'white'); //.show();
      } else {
        $('.ifDistance').css('background', 'red'); //.hide();
      }
    });
    $('#isOnCampusClass').on('change', function() {
      if($(this).val() == 'yes') {
        $('.ifOnCampusClass').css('background', 'white'); //.show();
      } else {
        $('.ifOnCampusClass').css('background', 'red'); //.hide();
      }
    });
    $('#doesDrink').on('change', function() {
      if($(this).val() == 'yes') {
          $('.ifDrink').css('background', 'white'); //.show();
      } else {
          $('.ifDrink').css('background', 'red'); //.hide();
      }
    });
    $('#isTutoring').on('change', function() {
      if($(this).val() == 'yes') {
        $('.ifTutoring').css('background', 'white'); //.show();
        $('.ifNotTutoring').css('background', 'red'); //.hide();
      } else {
        $('.ifTutoring').css('background', 'red'); //.hide();
        $('.ifNotTutoring').css('background', 'white'); //.show();
      }
    });
    $('#didOrientation').on('change', function() {
      if($(this).val() == 'yes') {
        $('.ifOrientation').css('background', 'white'); //.show();
      } else {
        $('.ifOrientation').css('background', 'red'); //.hide();
      }
    });
    $('#isOrg').on('change', function() {
      if($(this).val() == 'yes') {
        $('.ifOrg').css('background', 'white'); //.show();
      } else {
        $('.ifOrg').css('background', 'red'); //.hide();
      }
    });
    $('#isOnCampus').on('change', function() {
      if($(this).val() == 'on') {
        $('.ifOnCampus').css('background', 'red'); //.hide();
        $('.ifNotOnCampus').css('background', 'white'); //.show();
      } else {
        $('.ifOnCampus').css('background', 'white'); //.show();
        $('.ifNotOnCampus').css('background', 'red'); //.hide();
      }
      if($(this).val() == 'on' || $('#isAway').val() == 'yes')  {
        $('.ifAwayOrIfOnCampus').css('background', 'white'); //.show();
      } else {
        $('.ifAwayOrIfOnCampus').css('background', 'red'); //.hide();
      }
    });
    $('#isAway').on('change', function() {
      if($(this).val() == 'no') {
        $('.ifAway').css('background', 'red'); //.hide();
      } else {
        $('.ifAway').css('background', 'white'); //.show();
      }
      if($(this).val() == 'yes' || $('#isOnCampus').val() == 'on')  {
        $('.ifAwayOrIfOnCampus').css('background', 'white'); //.show();
      } else {
        $('.ifAwayOrIfOnCampus').css('background', 'red'); //.hide();
      }
    });
    $('#doesWork').on('change', function() {
      if($(this).val() == 'yes') {
        $('.ifWork').css('background', 'white'); //.show();
      } else {
        $('.ifWork').css('background', 'red'); //.hide();
      }
    });
  });