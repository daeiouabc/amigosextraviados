/*Lanza evento para que se carge el .geoposition-widget */
$('#modal-form-perdidos').on('shown.bs.modal', function () {

	$('#modal-form-perdidos').trigger( "LoadMap" );

	$("#id_position_0").prop("readonly", true);
	$("#id_position_1").prop("readonly", true);
	$("#id_position_0").parent().parent().parent().hide();
	$("#id_position_1").parent().parent().parent().hide();
	$("#input-search").attr("class", 'form-control');
	$("#input-search").attr("placeholder", '¿Dónde se extravió?');
	$("#id_dirDesaparicion").hide();
});

/*Evita que se duplique el mapa cuando se abra y oculte el modal */
$('#modal-form-perdidos').on('hidden.bs.modal', function (e) {
  $('.geoposition-widget').children().remove();
});