// from data.js
var tableData = data;

// refer to table body from index.html
var tbody = d3.select("tbody"); 

// 1. loop through data and console.log each alien sighting
// 2. append a table row 'tr' for each sighting report object
// 3. use object.entries to console.log each weather report value
// 4. use d3 to append 1 cell per sighting report value
// 5. Use d3 to update each cell's text with date/time, city, state, country, shape, comment
// 6. Create handleclick function
// 7. Grab datetime value from filter
// 8. Check date and apply filter to table
// 9. Recreate the filtered table by applying the previous createTable function
// 10. Attach an event listener to filter button

function createTable(data) {
    tbody.html("");
    data.forEach(function(sightingReport) {
        console.log(sightingReport);
        var row = tbody.append("tr");
        Object.values(sightingReport).forEach((value) => {
        console.log(value);
        var cell = row.append("td");
        cell.text(value);
        });
    });
}

function handleClick() {
    var datetime = d3.select("#datetime");
    var inputDate = datetime.property("value");
    if (inputDate) {
        tableData = tableData.filter(row => row.datetime === inputDate);
    }
    createTable(tableData);
}

d3.selectAll("#filter-btn").on("click", handleClick);

createTable(tableData);

