$(function () {

    function run(){
      guys.css('right', startPos);
      guys.animate({right: -1270}, 15000, 'linear')
    };

     var screenWidth = $(document).width();
     var startPos = screenWidth;
     var guys = $('#guys');
     run();
     setInterval(function() {
       run();
     }, 16000);

});
