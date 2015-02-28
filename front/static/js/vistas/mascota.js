var mascota = {};

/*******************/
/*FUNCIONES PARA LISTAR MASCOTAS*/

/*Informa al usuario de que se está esperando a que se reciba la lista de mascotas*/
mascota.showLoadingList = function(){
	  	console.log("MSG:Loading...");
	  	this.contenedor.append('<div id="msg-loading">Loading</div>');
};
/*Oculta lo anterior*/
mascota.hideLoadingList = function(){
	  	console.log("MSG:Loaded");
	  	$("#msg-loading").remove();
};

/*Muestra un error al usuario, en caso de que haya habido un error obteniendo las mascotas*/
mascota.showErrorList = function(code){
	  	console.log("MSG:Error");
	  	this.contenedor.append('<div id="msg-error">Error '+code+'</div>');
};
mascota.hideErrorList = function(){
		$("#msg-error").remove();  	
};

/*Renderiza la lista de mascotas obtenidas*/
mascota.showMascotas = function(){
	  	console.log("ACCION:Muestro mascotas");	  	
	  	var html = '';

	  	//si la lista es de perdidos
	  	if(this.json.perdidos)
	  	{
	  		$.each( this.json.perdidos, function( key, val ) {
	  			html += '<div class="perdido" data-id="'+val.id+'">';
	  			html += '<a href="'+window.location.pathname + val.id+'">';
    			html += '<p>'+val.nombre+'</p>';
    			html += '<img src="'+val.thumb+'"/>';
    			html += '</a>';
    			html += '<p>'+val.dirDesaparicion+'</p>';
    			html += '<p>'+jQuery.timeago(val.fechaPublicacion)+'</p>';
    			html += '<p>'+val.comments_count+' comentarios</p>';
    			html += '</div>';
 			
  			});

	  	}
	  	//si la lista es de adoptados
	  	if(this.json.adopciones)
	  	{
	  		$.each( this.json.adopciones, function( key, val ) {
    			html += '<div class="adopcion" data-id="'+val.id+'">';
    			html += '<a href="'+window.location.pathname + val.id+'">';
    			html += '<p>'+val.nombre+'</p>';
    			html += '<img src="'+val.thumb+'"/>';
    			html += '</a>';
    			html += '<p>'+val.dirContacto+'</p>';
    			html += '<p>'+jQuery.timeago(val.fechaPublicacion)+'</p>';
    			html += '<p>'+val.comments_count+' comentarios</p>';
    			html += '</div>';
  			});

	  	}
	  	

  		this.contenedor.append(html);
};


/*******************/
/*FUNCIONES PARA ENVIAR MASCOTA*/

/*obtiene un json de los valores del formulario*/
mascota.getDataForm = function(){
		return this.formulario.serialize();
};

/*Informa al usuario de que se está enviando la mascota*/
mascota.showSending = function(){
		console.log("MSG:Sending...");
};
/*Oculta el mensaje anterior*/
mascota.hideSending = function(){
		console.log("hide sending...");
};

/*Muestra un error al usuario, en caso de que haya habido un error enviando la mascota*/
mascota.showErrorSending = function(code, details){
		console.log("MSG:Error sending");
		console.log(code);
		console.log(details);
};