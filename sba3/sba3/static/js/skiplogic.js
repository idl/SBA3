  $('document').ready(function() {
    // classification
    $('#p1q1').change(function() {
      if($(this).val() == 'master' || $(this).val() == 'doctorate') {
        $('.ifNotGrad').css('background', 'red'); //.hide(); //
        $('.ifNotGrad select option:first-child').val('NA');
        $('.ifNotGrad select').val('NA');
        $('.ifNotGrad input').val(-100);
      } else {
        $('.ifNotGrad').show(); //.css('background', 'white')
        $('.ifNotGrad select option:first-child').val('');
        $('.ifNotGrad select').val('');
        $('.ifNotGrad input').val('');
      }
    });
    // isDistance
    $('#p1q4').change(function() {
      if($(this).val() == 'yes') {
        $('.ifDistance').show(); //.css('background', 'white')
        $('.ifDistance select option:first-child').val('');
        $('.ifDistance select').val('');
        $('.ifDistance input').val('');
      } else {
        $('.ifDistance').css('background', 'red'); //.hide(); //
        $('.ifDistance select option:first-child').val('NA');
        $('.ifDistance select').val('NA');
        $('.ifDistance input').val(-100);
      }
    });
    // isOnCampusClass
    $('#p1q5').change(function() {
      if($(this).val() == 'yes') {
        $('.ifOnCampusClass').show(); //.css('background', 'white')
        $('.ifOnCampusClass select option:first-child').val('');
        $('.ifOnCampusClass select').val('');
        $('.ifOnCampusClass input').val('');
      } else {
        $('.ifOnCampusClass').css('background', 'red'); //.hide(); //
        $('.ifOnCampusClass select option:first-child').val('NA');
        $('.ifOnCampusClass select').val('NA');
        $('.ifOnCampusClass input').val(-100);
      }
    });
    // isTutoring
    $('#p3q1').change(function() {
      if($(this).val() == 'yes') {
        $('.ifTutoring').show(); //.css('background', 'white')
        $('.ifTutoring select option:first-child').val('');
        $('.ifTutoring select').val('');
        $('.ifTutoring input').val('');

        $('.ifNotTutoring').css('background', 'red'); //.hide(); //
        $('.ifNotTutoring select option:first-child').val('NA');
        $('.ifNotTutoring select').val('NA');
        $('.ifNotTutoring input').val(-100);
      } else {
        $('.ifTutoring').css('background', 'red'); //.hide(); //
        $('.ifTutoring select option:first-child').val('NA');
        $('.ifTutoring select').val('NA');
        $('.ifTutoring input').val(-100);

        $('.ifNotTutoring').show(); //.css('background', 'white')
        $('.ifNotTutoring select option:first-child').val('');
        $('.ifNotTutoring select').val('');
        $('.ifNotTutoring input').val('');
      }
    });
    // didOrientation
    $('#p8q1').change(function() {
      if($(this).val() == 'yes') {
        $('.ifOrientation').show(); //.css('background', 'white')
        $('.ifOrientation select option:first-child').val('');
        $('.ifOrientation select').val('');
        $('.ifOrientation input').val('');
      } else {
        $('.ifOrientation').css('background', 'red'); //.hide(); //
        $('.ifOrientation select option:first-child').val('NA');
        $('.ifOrientation select').val('NA');
        $('.ifOrientation input').val(-100);
      }
    });
    // isOrg
    $('#p9q1').change(function() {
      if($(this).val() == 'yes') {
        $('.ifOrg').show(); //.css('background', 'white')
        $('.ifOrg select option:first-child').val('');
        $('.ifOrg select').val('');
        $('.ifOrg input').val('');
      } else {
        $('.ifOrg').css('background', 'red'); //.hide(); //
        $('.ifOrg select option:first-child').val('NA');
        $('.ifOrg select').val('NA');
        $('.ifOrg input').val(-100);
      }
    });
    // isOnCampus
    $('#p9q3').change(function() {
      if($(this).val() == 'on') {
        $('.ifOnCampus').css('background', 'red'); //.hide(); //
        $('.ifOnCampus select option:first-child').val('NA');
        $('.ifOnCampus select').val('NA');
        $('.ifOnCampus input').val(-100);

        $('.ifNotOnCampus').show(); //.css('background', 'white')
        $('.ifNotOnCampus select option:first-child').val('');
        $('.ifNotOnCampus select').val('');
        $('.ifNotOnCampus input').val('');
      } else {
        $('.ifOnCampus').show(); //.css('background', 'white')
        $('.ifOnCampus select option:first-child').val('');
        $('.ifOnCampus select').val('');
        $('.ifOnCampus input').val('');

        $('.ifNotOnCampus').css('background', 'red'); //.hide(); //
        $('.ifNotOnCampus select option:first-child').val('NA');
        $('.ifNotOnCampus select').val('NA');
        $('.ifNotOnCampus input').val(-100);
      }
      if($(this).val() == 'on' || $('#isAway').val() == 'yes')  {
        $('.ifAwayOrIfOnCampus').show(); //.css('background', 'white')
        $('.ifAwayOrIfOnCampus select option:first-child').val('');
        $('.ifAwayOrIfOnCampus select').val('');
        $('.ifAwayOrIfOnCampus input').val('');
      } else {
        $('.ifAwayOrIfOnCampus').css('background', 'red'); //.hide(); //
        $('.ifAwayOrIfOnCampus select option:first-child').val('NA');
        $('.ifAwayOrIfOnCampus select').val('NA');
        $('.ifAwayOrIfOnCampus input').val(-100);
      }
    });
    // isAway
    $('#p9q4').change(function() {
      if($(this).val() == 'no') {
        $('.ifAway').css('background', 'red'); //.hide(); //
        $('.ifAway select option:first-child').val('NA');
        $('.ifAway select').val('NA');
        $('.ifAway input').val(-100);
      } else {
        $('.ifAway').show(); //.css('background', 'white')
        $('.ifAway select option:first-child').val('');
        $('.ifAway select').val('');
        $('.ifAway input').val('');
      }
      if($(this).val() == 'yes' || $('#isOnCampus').val() == 'on')  {
        $('.ifAwayOrIfOnCampus').show(); //.css('background', 'white')
        $('.ifAwayOrIfOnCampus select option:first-child').val('');
        $('.ifAwayOrIfOnCampus select').val('');
        $('.ifAwayOrIfOnCampus input').val('');
      } else {
        $('.ifAwayOrIfOnCampus').css('background', 'red'); //.hide(); //
        $('.ifAwayOrIfOnCampus select option:first-child').val('NA');
        $('.ifAwayOrIfOnCampus select').val('NA');
        $('.ifAwayOrIfOnCampus input').val(-100);
      }
    });
    // doesDrink
    $('#p9q7').change(function() {
      if($(this).val() == 'yes') {
          $('.ifDrink').show(); //.css('background', 'white')
        $('.ifDrink select option:first-child').val('');
        $('.ifDrink select').val('');
        $('.ifDrink input').val('');
      } else {
          $('.ifDrink').css('background', 'red'); //.hide(); //
        $('.ifDrink select option:first-child').val('NA');
        $('.ifDrink select').val('NA');
        $('.ifDrink input').val(-100);
      }
    });
    // doesWork
    $('#p11q3').change(function() {
      if($(this).val() == 'yes') {
        $('.ifWork').show(); //.css('background', 'white')
        $('.ifWork select option:first-child').val('');
        $('.ifWork select').val('');
        $('.ifWork input').val('');
      } else {
        $('.ifWork').css('background', 'red'); //.hide(); //
        $('.ifWork select option:first-child').val('NA');
        $('.ifWork select').val('NA');
        $('.ifWork input').val(-100);
      }
    });
  });