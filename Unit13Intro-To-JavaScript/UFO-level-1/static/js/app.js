// from data.js
var tableData = data;

// refer to table body from index.html
var tbody = d3.select("tbody");

// 1. loop through data and console.log each alien sighting
// 2. append a table row 'tr' for each sighting report object
// 3. use object.entries to console.log each weather report value
// 4. use d3 to append 1 cell per sighting report value
// 5. Use d3 to update each cell's text with date/time, city, state, country, shape, comment
tableData.forEach(function(sightingReport) {
    console.log(sightingReport);
    var row = tbody.append("tr");
    Object.defineProperties(sightingReport).forEach(function([key, value]) {
        console.log(key, value);
        var cell = row.append("td");
        cell.text(value);
    });
});




