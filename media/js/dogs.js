var siberia = new google.maps.LatLng(60, 105);
var newyork = new google.maps.LatLng(40.69847032728747, -73.9514422416687);
var browserSupportFlag = new Boolean();
var map;
var infowindow = new google.maps.InfoWindow();
var initialLocation;
var request;
var markers = {};
var notSet = true;

//WEB_SOCKET_SWF_LOCATION = '/static/lib/vendor/web-socket-js/WebSocketMain.swf';


$(document).ready(function(){

    //----------------------------------
    // create map
    //----------------------------------

    var myOptions = {
        zoom: 15,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
   // map.enableRotation();


    $('#goto').click(function(event){
        map.panTo(initialLocation);
        map.setZoom(17);
        return false;
    });

    var reset = true;


    getLocation();
    map.setCenter(initialLocation);





      google.maps.event.addListener(map, 'idle', function() {
    	  reset = true;
    	  var bounds = map.getBounds();
    	  if (bounds) {
    		  var ne = bounds.getNorthEast();
    		  var sw = bounds.getSouthWest();
    		  msg = sw.lng()+','+ne.lat()+','+ne.lng()+','+sw.lat()+','+map.getZoom();
    		  console.log("sent: "+msg);
    	  }
      });

      google.maps.event.addListener(map, 'click', function(event) {
        alert(event);
      });





 // show hint in input fields
    $(".defaultText").focus(function(srcc)
    	    {
    	        if ($(this).val() == $(this)[0].title)
    	        {
    	            $(this).removeClass("defaultTextActive");
    	            $(this).val("");
    	        }
    	    });

    	    $(".defaultText").blur(function()
    	    {
    	        if ($(this).val() == "")
    	        {
    	            $(this).addClass("defaultTextActive");
    	            $(this).val($(this)[0].title);
    	        }
    	    });

    	    $(".defaultText").blur();

    	    $("form").submit(function() {
    	        $(".defaultText").each(function() {
    	            if($(this).val() == this.title) {
    	                $(this).val("");
    	            }
    	        });
    	    });


});




function getLocation() {
    if (navigator.geolocation) {
        browserSupportFlag = true;
        navigator.geolocation.getCurrentPosition(function(position) {
            initialLocation = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
            if (notSet) {
                map.setCenter(initialLocation);
                notSet = false;
            }
        }, function() {
            handleNoGeolocation(browserSupportFlag);
        });
    } else if (google.gears) {
        // Try Google Gears Geolocation
        browserSupportFlag = true;
        var geo = google.gears.factory.create('beta.geolocation');
        geo.getCurrentPosition(function(position) {
            initialLocation = new google.maps.LatLng(position.latitude, position.longitude);
        }, function() {
            handleNoGeolocation(browserSupportFlag);
        });
    } else {
        // Browser doesn't support Geolocation
        browserSupportFlag = false;
        handleNoGeolocation(browserSupportFlag);
    }
}

function handleNoGeolocation(errorFlag) {
    if (errorFlag == true) {
        initialLocation = newyork;
        contentString = "Error: The Geolocation service failed.";
    } else {
        initialLocation = siberia;
        contentString = "Error: Your browser doesn't support geolocation. Are you in Siberia?";
    }
    map.setCenter(initialLocation);
    //infowindow.setContent(contentString);
    //infowindow.setPosition(initialLocation);
    //infowindow.open(map);
}


var small = 'http://maps.google.com/mapfiles/ms/micons/red-dot.png'
var large = 'http://maps.google.com/mapfiles/ms/micons/yellow-dot.png'

function showPin(results) {


        for (i = 0; i < results.length; i++) {
        	var lat = results[i][0]
        	var lon = results[i][1]
            var uid = results[i][2];
            var count = parseInt(results[i][3]);
            marker = markers[uid]
            if (lat == null || lon == null) {
            	if (marker != null) {
            		marker.setMap(null);
                    delete markers[uid];
            	}
            } else {
            	if (marker == null) {
	                var marker = new google.maps.Marker({
	                    position: new google.maps.LatLng(lat,lon),
	                    map: map,
	                    icon: small,
	                    title:uid
	                });
	                markers[uid] = marker;
	            } else {
	                marker.setPosition(new google.maps.LatLng(lat,lon));
	            }
	            if (count > 30) {
		            marker.setIcon("http://gmaps-utility-library.googlecode.com/svn/trunk/markerclusterer/images/m4.png");
	            } else if (count > 6) {
		            marker.setIcon("http://gmaps-utility-library.googlecode.com/svn/trunk/markerclusterer/images/m3.png");
	            } else if (count > 3) {
		            marker.setIcon("http://gmaps-utility-library.googlecode.com/svn/trunk/markerclusterer/images/m2.png");
	            } else if (count > 1) {
		            marker.setIcon("http://gmaps-utility-library.googlecode.com/svn/trunk/markerclusterer/images/m1.png");
	            } else {
	                marker.setIcon(small);
	            }
	            marker.setTitle(uid +" "+ count)
            }

        }

}

function clearPins() {
	// Deletes all markers in the array by removing references to them
	for(var key in markers) {
		markers[key].setMap(null);
		delete markers[key];
	}
}