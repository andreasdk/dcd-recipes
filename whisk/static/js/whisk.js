//adds the 'scrolled' class to the navbar on scroll, changing the nav background color
$(function () {
    $(document).scroll(function(){
      var $nav = $("#navbar__whisk");
      $nav.toggleClass("scrolled", $(this).scrollTop() > $nav.height() );
    })
})