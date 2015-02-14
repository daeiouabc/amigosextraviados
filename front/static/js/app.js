var main = function() {

	$('#down').click(function(){
		$("body").animate({scrollTop:$('#slide2').offset().top}, 200);
	});

	$('#up').click(function(){
		$("body").animate({scrollTop:$('.head').offset().top}, 200);
	});


	$(window).scroll(function (event) {
    var scroll = $(window).scrollTop();
    // Do something
	    if(scroll >= $('#slide2').offset().top) {
			$('.info').animate({left:'0px'},200);	
		}
	});

	
	
	
};


$(document).ready(main);