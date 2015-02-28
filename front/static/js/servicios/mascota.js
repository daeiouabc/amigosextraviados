var servicioMascota = {};


servicioMascota.setCSRFToken = function(){
    //configura el csrftoken a la peticion ajax
  $.ajaxSetup({
      beforeSend: function(xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", 'skEa5MbGp75COJsPqoVFUINtQKS4nCTf');
      }
  });
};

servicioMascota.getList = function(url, contenedor){
  //div que va a contener la lista de perdidos
  mascota.contenedor = contenedor;
  console.log(mascota.contenedor)

  //se avisa de que se esta cargando la lista
  mascota.showLoadingList();


  
  $.getJSON( url, function(response) {
    mascota.json = response;
     
  })
    .fail(function(response) {
      console.log( "error" );
      mascota.showErrorList(response.status);
      console.log(response);
    })
    .always(function() {
      console.log( "complete (always)" );
      //se oculta el aviso de cargando
      mascota.hideLoadingList();
      //se muestra la lista
      mascota.showMascotas();
    });

};

servicioMascota.sendMascota = function(url, form){
  mascota.formulario = form;
  mascota.showSending();

  servicioMascota.setCSRFToken();
  $.ajax({
    url : url, 
        type : "POST",
        data: mascota.getDataForm(),
        async: false,
  })
    .done(function(response){
      console.log("Send");
    })
    .fail(function(response) {
      mascota.showErrorSending(response.status, response.responseText);
      //console.log(response);
    })
    .always(function(response){
      console.log( "complete (always)" );
      //se oculta el aviso de enviando
      mascota.hideSending();
    });

};