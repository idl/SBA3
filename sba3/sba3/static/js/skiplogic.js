  $('document').ready(function() {
    // classification
    $('#p1q1').change(function() {
      if($(this).val() == 'master' || $(this).val() == 'doctorate') {
        $('.ifNotGrad').css('background', 'red'); //.hide(); //
        $('.ifNotGrad select option:first-child').val('NA');
        $('.ifNotGrad select').val('NA');
        $('.ifNotGrad input').attr('min', -100).val(-100);
      } else {
        $('.ifNotGrad').show().css('background', 'lightblue');
        $('.ifNotGrad select option:first-child').val('');
        $('.ifNotGrad select').val('');
        $('.ifNotGrad input').attr('min', -2).val('');
      }
    });
    // isDistance
    $('#p1q4').change(function() {
      if($(this).val() == 'yes') {
        $('.ifDistance').show().css('background', 'lightblue');
        $('.ifDistance select option:first-child').val('');
        $('.ifDistance select').val('');
        $('.ifDistance input').attr('min', -2).val('');
      } else {
        $('.ifDistance').css('background', 'red'); //.hide(); //
        $('.ifDistance select option:first-child').val('NA');
        $('.ifDistance select').val('NA');
        $('.ifDistance input').attr('min', -100);
        $('.ifDistance input').val(-100);
      }
    });
    // isOnCampusClass
    $('#p1q5').change(function() {
      if($(this).val() == 'yes') {
        $('.ifOnCampusClass').show().css('background', 'lightblue');
        $('.ifOnCampusClass select option:first-child').val('');
        $('.ifOnCampusClass select').val('');
        $('.ifOnCampusClass input').attr('min', -2).val('');
      } else {
        $('.ifOnCampusClass').css('background', 'red'); //.hide(); //
        $('.ifOnCampusClass select option:first-child').val('NA');
        $('.ifOnCampusClass select').val('NA');
        $('.ifOnCampusClass input').attr('min', -100);
        $('.ifOnCampusClass input').val(-100);
      }
    });
    // isTutoring
    $('#p3q1').change(function() {
      if($(this).val() == 'yes') {
        $('.ifTutoring').show().css('background', 'lightblue');
        $('.ifTutoring select option:first-child').val('');
        $('.ifTutoring select').val('');
        $('.ifTutoring input').attr('min', -2).val('');

        $('.ifNotTutoring').css('background', 'red'); //.hide(); //
        $('.ifNotTutoring select option:first-child').val('NA');
        $('.ifNotTutoring select').val('NA');
        $('.ifNotTutoring input').attr('min', -2).val('');
      } else {
        $('.ifTutoring').css('background', 'red'); //.hide(); //
        $('.ifTutoring select option:first-child').val('NA');
        $('.ifTutoring select').val('NA');
        $('.ifTutoring input').attr('min', -100);
        $('.ifTutoring input').val(-100);

        $('.ifNotTutoring').show().css('background', 'lightblue');
        $('.ifNotTutoring select option:first-child').val('');
        $('.ifNotTutoring select').val('');
        $('.ifNotTutoring input').attr('min', -2).val('');
      }
    });
    // didOrientation
    $('#p8q1').change(function() {
      if($(this).val() == 'yes') {
        $('.ifOrientation').show().css('background', 'lightblue');
        $('.ifOrientation select option:first-child').val('');
        $('.ifOrientation select').val('');
        $('.ifOrientation input').attr('min', -2).val('');
      } else {
        $('.ifOrientation').css('background', 'red'); //.hide(); //
        $('.ifOrientation select option:first-child').val('NA');
        $('.ifOrientation select').val('NA');
        $('.ifOrientation input').attr('min', -100);
        $('.ifOrientation input').val(-100);
      }
    });
    // isOrg
    $('#p9q1').change(function() {
      if($(this).val() == 'yes') {
        $('.ifOrg').show().css('background', 'lightblue');
        $('.ifOrg select option:first-child').val('');
        $('.ifOrg select').val('');
        $('.ifOrg input').attr('min', -2).val('');
      } else {
        $('.ifOrg').css('background', 'red'); //.hide(); //
        $('.ifOrg select option:first-child').val('NA');
        $('.ifOrg select').val('NA');
        $('.ifOrg input').attr('min', -100);
        $('.ifOrg input').val(-100);
      }
    });
    // isOnCampus
    $('#p9q3').change(function() {
      if($(this).val() == 'on') {
        $('.ifOnCampus').css('background', 'red'); //.hide(); //
        $('.ifOnCampus select option:first-child').val('NA');
        $('.ifOnCampus select').val('NA');
        $('.ifOnCampus input').attr('min', -100);
        $('.ifOnCampus input').val(-100);

        $('.ifNotOnCampus').show().css('background', 'lightblue');
        $('.ifNotOnCampus select option:first-child').val('');
        $('.ifNotOnCampus select').val('');
        $('.ifNotOnCampus input').attr('min', -2).val('');
      } else {
        $('.ifOnCampus').show().css('background', 'lightblue');
        $('.ifOnCampus select option:first-child').val('');
        $('.ifOnCampus select').val('');
        $('.ifOnCampus input').attr('min', -2).val('');

        $('.ifNotOnCampus').css('background', 'red'); //.hide(); //
        $('.ifNotOnCampus select option:first-child').val('NA');
        $('.ifNotOnCampus select').val('NA');
        $('.ifNotOnCampus input').attr('min', -100);
        $('.ifNotOnCampus input').val(-100);
      }
      if($(this).val() == 'on' || $('#isAway').val() == 'yes')  {
        $('.ifAwayOrIfOnCampus').show().css('background', 'lightblue');
        $('.ifAwayOrIfOnCampus select option:first-child').val('');
        $('.ifAwayOrIfOnCampus select').val('');
        $('.ifAwayOrIfOnCampus input').attr('min', -2).val('');
      } else {
        $('.ifAwayOrIfOnCampus').css('background', 'red'); //.hide(); //
        $('.ifAwayOrIfOnCampus select option:first-child').val('NA');
        $('.ifAwayOrIfOnCampus select').val('NA');
        $('.ifAwayOrIfOnCampus input').attr('min', -100);
        $('.ifAwayOrIfOnCampus input').val(-100);
      }
    });
    // isAway
    $('#p9q4').change(function() {
      if($(this).val() == 'no') {
        $('.ifAway').css('background', 'red'); //.hide(); //
        $('.ifAway select option:first-child').val('NA');
        $('.ifAway select').val('NA');
        $('.ifAway input').attr('min', -100).val(-100);
      } else {
        $('.ifAway').show().css('background', 'lightblue');
        $('.ifAway select option:first-child').val('');
        $('.ifAway select').val('');
        $('.ifAway input').attr('min', -2).val('');
      }
      if($(this).val() == 'yes' || $('#isOnCampus').val() == 'on')  {
        $('.ifAwayOrIfOnCampus').show().css('background', 'lightblue');
        $('.ifAwayOrIfOnCampus select option:first-child').val('');
        $('.ifAwayOrIfOnCampus select').val('');
        $('.ifAwayOrIfOnCampus input').attr('min', -2).val('');
      } else {
        $('.ifAwayOrIfOnCampus').css('background', 'red'); //.hide(); //
        $('.ifAwayOrIfOnCampus select option:first-child').val('NA');
        $('.ifAwayOrIfOnCampus select').val('NA');
        $('.ifAwayOrIfOnCampus input').attr('min', -100);
        $('.ifAwayOrIfOnCampus input').val(-100);
      }
    });
    // doesDrink
    $('#p9q7').change(function() {
      if($(this).val() == 'yes') {
        $('.ifDrink').show().css('background', 'lightblue');
        $('.ifDrink select option:first-child').val('');
        $('.ifDrink select').val('');
        $('.ifDrink input').attr('min', -2).val('');
      } else {
        $('.ifDrink').css('background', 'red'); //.hide(); //
        $('.ifDrink select option:first-child').val('NA');
        $('.ifDrink select').val('NA');
        $('.ifDrink input').attr('min', -100);
        $('.ifDrink input').val(-100);
      }
    });
    // doesWork
    $('#p11q3').change(function() {
      if($(this).val() == 'yes') {
        $('.ifWork').show().css('background', 'lightblue');
        $('.ifWork select option:first-child').val('');
        $('.ifWork select').val('');
        $('.ifWork input').attr('min', -2).val('');
      } else {
        $('.ifWork').css('background', 'red'); //.hide(); //
        $('.ifWork select option:first-child').val('NA');
        $('.ifWork select').val('NA');
        $('.ifWork input').attr('min', -100);
        $('.ifWork input').val(-100);
      }
    });
  });