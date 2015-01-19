var result;

function geoSuccess(position) {
  console.log(position);
  result = {
  	POSITION_AVAILABLE: 1,
  	status: "OK",
  	latitude: position.coords.latitude,
  	longitude: position.coords.longitude
  };
  loadMap(result);
}

function geoError(err) {
	console.log(err);
	result = {
		POSITION_AVAILABLE: 0,
		latitude: 3,
		longitude: 3
	};  	
  	switch(err.code) {
        case err.PERMISSION_DENIED:
            result.status = 'User denied the request for Geolocation.';
            break;
        case err.POSITION_UNAVAILABLE:
            result.status = 'Location information is unavailable.';
            break;
        case err.TIMEOUT:
            result.status = 'The request to get user location timed out.';
            break;
        case err.UNKNOWN_ERROR:
            result.status = 'An unknown error occurred.';
            break;
    }

    loadMap(result);
}

function checkLocation () {
  if (navigator.geolocation) {
  	var options = {
    		enableHighAccuracy: true,
    		timeout: 5000,
    		maximumAge: 0
  	};
  	navigator.geolocation.getCurrentPosition(geoSuccess, geoError, options);
  }
  else {
  	console.log('Browser no not supporte geolocation API');
  	result = {
  		POSITION_AVAILABLE: 0,
  		status: 'Browser no not supporte geolocation API',
  		latitude: 3,
  		longitude: 3
  	};  	
  	  loadMap(result);
  }
}

