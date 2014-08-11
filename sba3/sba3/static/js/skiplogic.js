  $('document').ready(function() {
    // classification
    $('#p1q1').on('change', function() {
      if($(this).val() == 'master' || $(this).val() == 'doctorate') {
        $('.ifNotGrad').hide(); //.css('background', 'red'); 
        $('.ifNotGrad select option:first-child').val('NA');
        $('.ifNotGrad select').val('NA');
        $('.ifNotGrad input').val(0);
      } else {
        $('.ifNotGrad').show(); //.css('background', 'white')
        $('.ifNotGrad select option:first-child').val('');
        $('.ifNotGrad select').val('');
        $('.ifNotGrad input').val('');
      }
    });
    // isDistance
    $('#p1q4').on('change', function() {
      if($(this).val() == 'yes') {
        $('.ifDistance').show(); //.css('background', 'white')
        $('.ifDistance select option:first-child').val('');
        $('.ifDistance select').val('');
        $('.ifDistance input').val('');
      } else {
        $('.ifDistance').hide(); //.css('background', 'red'); 
        $('.ifDistance select option:first-child').val('NA');
        $('.ifDistance select').val('NA');
        $('.ifDistance input').val(0);
      }
    });
    // isOnCampusClass
    $('#p1q5').on('change', function() {
      if($(this).val() == 'yes') {
        $('.ifOnCampusClass').show(); //.css('background', 'white')
        $('.ifOnCampusClass select option:first-child').val('');
        $('.ifOnCampusClass select').val('');
        $('.ifOnCampusClass input').val('');
      } else {
        $('.ifOnCampusClass').hide(); //.css('background', 'red'); 
        $('.ifOnCampusClass select option:first-child').val('NA');
        $('.ifOnCampusClass select').val('NA');
        $('.ifOnCampusClass input').val(0);
      }
    });
    // isTutoring
    $('#p3q1').on('change', function() {
      if($(this).val() == 'yes') {
        $('.ifTutoring').show(); //.css('background', 'white')
        $('.ifTutoring select option:first-child').val('');
        $('.ifTutoring select').val('');
        $('.ifTutoring input').val('');

        $('.ifNotTutoring').hide(); //.css('background', 'red'); 
        $('.ifNotTutoring select option:first-child').val('NA');
        $('.ifNotTutoring select').val('NA');
        $('.ifNotTutoring input').val(0);
      } else {
        $('.ifTutoring').hide(); //.css('background', 'red'); 
        $('.ifTutoring select option:first-child').val('NA');
        $('.ifTutoring select').val('NA');
        $('.ifTutoring input').val(0);

        $('.ifNotTutoring').show(); //.css('background', 'white')
        $('.ifNotTutoring select option:first-child').val('');
        $('.ifNotTutoring select').val('');
        $('.ifNotTutoring input').val('');
      }
    });
    // didOrientation
    $('#p8q1').on('change', function() {
      if($(this).val() == 'yes') {
        $('.ifOrientation').show(); //.css('background', 'white')
        $('.ifOrientation select option:first-child').val('');
        $('.ifOrientation select').val('');
        $('.ifOrientation input').val('');
      } else {
        $('.ifOrientation').hide(); //.css('background', 'red'); 
        $('.ifOrientation select option:first-child').val('NA');
        $('.ifOrientation select').val('NA');
        $('.ifOrientation input').val(0);
      }
    });
    // isOrg
    $('#p9q1').on('change', function() {
      if($(this).val() == 'yes') {
        $('.ifOrg').show(); //.css('background', 'white')
        $('.ifOrg select option:first-child').val('');
        $('.ifOrg select').val('');
        $('.ifOrg input').val('');
      } else {
        $('.ifOrg').hide(); //.css('background', 'red'); 
        $('.ifOrg select option:first-child').val('NA');
        $('.ifOrg select').val('NA');
        $('.ifOrg input').val(0);
      }
    });
    // isOnCampus
    $('#p9q3').on('change', function() {
      if($(this).val() == 'on') {
        $('.ifOnCampus').hide(); //.css('background', 'red'); 
        $('.ifOnCampus select option:first-child').val('NA');
        $('.ifOnCampus select').val('NA');
        $('.ifOnCampus input').val(0);

        $('.ifNotOnCampus').show(); //.css('background', 'white')
        $('.ifNotOnCampus select option:first-child').val('');
        $('.ifNotOnCampus select').val('');
        $('.ifNotOnCampus input').val('');
      } else {
        $('.ifOnCampus').show(); //.css('background', 'white')
        $('.ifOnCampus select option:first-child').val('');
        $('.ifOnCampus select').val('');
        $('.ifOnCampus input').val('');

        $('.ifNotOnCampus').hide(); //.css('background', 'red'); 
        $('.ifNotOnCampus select option:first-child').val('NA');
        $('.ifNotOnCampus select').val('NA');
        $('.ifNotOnCampus input').val(0);
      }
      if($(this).val() == 'on' || $('#isAway').val() == 'yes')  {
        $('.ifAwayOrIfOnCampus').show(); //.css('background', 'white')
        $('.ifAwayOrIfOnCampus select option:first-child').val('');
        $('.ifAwayOrIfOnCampus select').val('');
        $('.ifAwayOrIfOnCampus input').val('');
      } else {
        $('.ifAwayOrIfOnCampus').hide(); //.css('background', 'red'); 
        $('.ifAwayOrIfOnCampus select option:first-child').val('NA');
        $('.ifAwayOrIfOnCampus select').val('NA');
        $('.ifAwayOrIfOnCampus input').val(0);
      }
    });
    // isAway
    $('#p9q4').on('change', function() {
      if($(this).val() == 'no') {
        $('.ifAway').hide(); //.css('background', 'red'); 
        $('.ifAway select option:first-child').val('NA');
        $('.ifAway select').val('NA');
        $('.ifAway input').val(0);
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
        $('.ifAwayOrIfOnCampus').hide(); //.css('background', 'red'); 
        $('.ifAwayOrIfOnCampus select option:first-child').val('NA');
        $('.ifAwayOrIfOnCampus select').val('NA');
        $('.ifAwayOrIfOnCampus input').val(0);
      }
    });
    // doesDrink
    $('#p9q7').on('change', function() {
      if($(this).val() == 'yes') {
          $('.ifDrink').show(); //.css('background', 'white')
        $('.ifDrink select option:first-child').val('');
        $('.ifDrink select').val('');
        $('.ifDrink input').val('');
      } else {
          $('.ifDrink').hide(); //.css('background', 'red'); 
        $('.ifDrink select option:first-child').val('NA');
        $('.ifDrink select').val('NA');
        $('.ifDrink input').val(0);
      }
    });
    // doesWork
    $('#p11q3').on('change', function() {
      if($(this).val() == 'yes') {
        $('.ifWork').show(); //.css('background', 'white')
        $('.ifWork select option:first-child').val('');
        $('.ifWork select').val('');
        $('.ifWork input').val('');
      } else {
        $('.ifWork').hide(); //.css('background', 'red'); 
        $('.ifWork select option:first-child').val('NA');
        $('.ifWork select').val('NA');
        $('.ifWork input').val(0);
      }
    });
  });