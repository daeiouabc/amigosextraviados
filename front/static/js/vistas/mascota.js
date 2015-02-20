var mascota = {};

/*******************/
/*FUNCIONES PARA LISTAR MASCOTAS*/

/*Informa al usuario de que se está esperando a que se reciba la lista de mascotas*/
mascota.showLoadingList = function(){
	  	console.log("Loading...");
	  	$("#"+this.contenedor).append('<div id="msg-loading">Loading</div>');
};
/*Oculta lo anterior*/
mascota.hideLoadingList = function(){
	  	console.log("Loaded");
	  	$("#msg-loading").remove();
};

/*Muestra un error al usuario, en caso de que haya habido un error obteniendo las mascotas*/
mascota.showErrorList = function(code){
	  	console.log("Error");
	  	$("#"+this.contenedor).append('<div id="msg-error">Error '+code+'</div>');
};
mascota.hideErrorList = function(){
		$("#msg-error").remove();  	
};

/*Renderiza la lista de mascotas obtenidas*/
mascota.showMascotas = function(){
	  	console.log("Los muestro");	  	
	  	var html = '';

	  	//si la lista es de perdidos
	  	if(this.json.perdidos)
	  	{
	  		$.each( this.json.perdidos, function( key, val ) {
    			html += '<div id="perd-'+val.id+'" value='+val.id+'><p>'+val.nombre+'</p><img src="'+val.thumb+'"/><p>'+val.comments_count+' comentarios</p></div>';
  			});

	  	}
	  	

  		$("#"+this.contenedor).append(html);
};


/*******************/
/*FUNCIONES PARA ENVIAR MASCOTA*/

/*obtiene un json de los valores del formulario*/
mascota.getDataForm = function(){
		return $("#"+this.formulario).serialize();
};

/*Informa al usuario de que se está enviando la mascota*/
mascota.showSending = function(){
		console.log("Sending...");
};
/*Oculta el mensaje anterior*/
mascota.hideSending = function(){
		console.log("hide sending...");
};

/*Muestra un error al usuario, en caso de que haya habido un error enviando la mascota*/
mascota.showErrorSending = function(code, details){
		console.log("Error sending");
		console.log(code);
		console.log(details);
};