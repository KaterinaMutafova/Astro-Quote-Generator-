$(function(){
    $("img.lazy").lazyload({ effect : "fadeIn", });
    $("#btnIcon").on("click",function(){ $(".othericons").toggle(); return false; });
    if($("div#back-top").length == 0){$("body").append("<div id=\"back-top\"><a href=\"#top\"><span>Top</span></a></div>");};$("div#back-top").css('visibility', 'visible');
    $("div#back-top").hide();
    $(window).scroll(function () { if ($(this).scrollTop() > 100) { $('div#back-top').fadeIn(); } else { $('div#back-top').fadeOut(); }});
    $('div#back-top a').click(function () { $( 'html, body' ).animate( { scrollTop: 0 }, 'slow' ); return false; });
});