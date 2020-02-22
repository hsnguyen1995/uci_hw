// dependencies
var mapboxURL = "https://api.mapbox.com/styles/v1/{username}/cjfon2bd904iy2spdjzs1infc?access_token={accessToken}";
var usgsURL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson";
var username = "huynerthaitea"
var accessToken = "pk.eyJ1IjoiaHV5bmVydGhhaXRlYSIsImEiOiJjazRkazd3aW8wM3F2M21wZ2FqZnVyam9kIn0.HGodn9Qt-souIhNbWlbK1g"

var quakeLayer = new L.LayerGroup();

// use d3.json to request data
d3.json(usgsURL, function(json) {
    // resize each marker of magnitudes
    function resizeMarker(mag) {
        return mag * 3;
    };
    function color(mag) {
        return mag > 5 ? "darkred":
            mag > 4 ? "red":
            mag > 3 ? "orange":
            mag > 2 ? "yellow":
            mag > 1 ? "yellowgreen":
                "green";
    }
    // add geojson layer and add circlemarker
    L.geoJSON(json.features, {
        pointToLayer: function(marker, latlng) {
            return L.circleMarker(latlng, {radius: resizeMarker(marker.properties.mag), {fillcolor: color(marker.properties.mag)}});
        },
        style: function style(marker) {
            return {
                opacity:1,
                fillOpacity:1,
                weight: 0.3,
                color: "black",
            };
        };
    }).addTo(quakeLayer);
});

function createMap() {
    var map = L.tileLayer(mapboxURL, {
        username: username,
        accessToken: accessToken
    });
}

