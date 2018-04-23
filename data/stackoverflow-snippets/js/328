function geocodeLatLng(){
  var input = document.getElementById("latlng").value;
  var w = window.open('', '_blank'); //you must use predefined window name here for IE.
  var head = w.document.getElementsByTagName('head')[0];
  w.document.head.innerHTML = '<title>Simple Map</title></head>';
  w.document.body.innerHTML = '<body><H1>Loading</H1><div id="map_canvas" style="display: block; width: 500px; height: 300px; margin: 0; padding: 0;"></div></body>';
  var loadScript = w.document.createElement('script');
  //Link to script that load google maps from hidden elements.
  loadScript.type = "text/javascript";
  loadScript.async = true;
  loadScript.src = "https://maps.googleapis.com/maps/api/js?sensor=false&callback=initialize";
  var googleMapScript = w.document.createElement('script');
  //Link to google maps js, use callback=... URL parameter to setup the calling function after google maps load.
  googleMapScript.type = "text/javascript";
  googleMapScript.async = false;
  googleMapScript.text = 'var map;';
  googleMapScript.text += 'function initialize() {';
  googleMapScript.text += '  var latlng = new google.maps.LatLng('+input+');';
  googleMapScript.text += '  var mapOptions = {';
  googleMapScript.text += '    center: latlng,';
  googleMapScript.text += '    zoom: 11, ';
  googleMapScript.text += '  };';
  googleMapScript.text += '  map = new google.maps.Map(document.getElementById("map_canvas"), mapOptions);';
  googleMapScript.text += '  var marker = new google.maps.Marker({';
  googleMapScript.text += '    position: latlng,';
  googleMapScript.text += '    map: map';
  googleMapScript.text += ' });';
  googleMapScript.text += 'var geocoder = new google.maps.Geocoder;';
  googleMapScript.text += 'var infowindow = new google.maps.InfoWindow;';
  googleMapScript.text += 'geocoder.geocode({"location": latlng}, function(results, status) {';
  googleMapScript.text += ' infowindow.setContent(results[0].formatted_address);';
  googleMapScript.text += ' infowindow.open(map, marker);';
  googleMapScript.text += '});';
  googleMapScript.text += '}';
  head.appendChild(loadScript);
  head.appendChild(googleMapScript);
}
