    $('.inputProperty').on('change', function() {
    $('.inputProperty').not(this).prop('checked', false);
  });
    $('.bedroomProperty').on('change', function() {
    $('.bedroomProperty').not(this).prop('checked', false);
  });
    $('.furnishedProperty').on('change', function() {
    $('.furnishedProperty').not(this).prop('checked', false);
  });
$(".expander").click(function(){
    $(".formMobile").slideToggle();
  });
