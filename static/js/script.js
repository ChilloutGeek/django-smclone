var x = $('a')

x.css('text-decoration', 'none')


$(document).ready(function(){
    $(".dropdown").click(function(){
        $(this).toggleClass("active");        
    })
});