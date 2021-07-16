$(document).ready(function(){

    var x = $('a')

    x.css('text-decoration', 'none')
    
    $(window).on("scroll", function() {
        //page height
        var scrollHeight = $(document).height();
        //scroll position
        var scrollPos = $(window).height() + $(window).scrollTop();
        // fire if the scroll position is 300 pixels above the bottom of the page
        if(((scrollHeight - 300) >= scrollPos) / scrollHeight == 0){
          $('.load-more-days-button').click();
         }
       });

    })