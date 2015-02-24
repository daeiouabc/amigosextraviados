var main = function() {
	$('html, body').animate({
    	scrollTop: $("#registro").offset().top-50}, 1000);


	$('#down').click(function(){
		$("body").animate({scrollTop:$('#slide2').offset().top}, 200);
	});

	$('#up').click(function(){
		$("body").animate({scrollTop:$('#head').offset().top}, 200);
		
	});

	$('#iniciaSesion').click(function(e){
		e.preventDefault();
		/*$('.registro').fadeOut();*/
		$('#registro').toggle();
		$('#sesion').fadeIn();
		var offset = $("#sesion").offset();
		$('html, body').stop().animate({
    		scrollTop: offset.top-50}, 600);

	});

	$('#iniciaRegistro').click(function(e){
		e.preventDefault();
		/*$('.registro').fadeOut();*/
		$('#sesion').toggle();
		$('#registro').fadeIn();
		var offset = $("#registro").offset();
		$('html, body').stop().animate({
    		scrollTop: offset.top-50}, 600);
	});


	/*$(window).scroll(function (event) {
    var scroll = $(window).scrollTop();
    // Do something
	    if(scroll >=($('#slide2').offset().top)-50) {
			$('.info').animate({left:'0px'},200);
		}else{
			$('.info').animate({left:'450px'},200);
		}
	});*/

	
	
	
};

$(document).ready(main);