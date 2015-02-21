var main = function() {

	$('#down').click(function(){
		$("body").animate({scrollTop:$('#slide2').offset().top}, 200);
	});

	$('#up').click(function(){
		$("body").animate({scrollTop:$('#head').offset().top}, 200);
		
	});

	$('#iniciaSesion').click(function(){
		/*$('.registro').fadeOut();*/
		$('#registro').toggle();
		$('#sesion').fadeIn();
	});

	$('#iniciaRegistro').click(function(){
		/*$('.registro').fadeOut();*/
		$('#sesion').toggle();
		$('#registro').fadeIn();
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