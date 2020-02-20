// metadata keys: id, ethnicity, gender, age, location, bbytpe, wfreq

// Use D3 to read samples.json
// Display the sample metadata, i.e., an individual's demographic information.
// Display each key-value pair from the metadata JSON object somewhere on the page.
function getJSON(selection) {
    var path = "static/data/samples.json"
    d3.json(path).then(function(d) {
        var jsondata = d.metadata;
        // console.log(jsondata);
        var samp = d3.select("#sample-metadata");
        samp.html("");
        var selectedData = jsondata.filter(md => md.id == selection);
        // console.log(selectedData);
        var result = selectedData[0];
        console.log(result);

        Object.entries(result).forEach(([key, value]) => {
            samp.append("p").text(key + ":" + value + "\n");
        });
    });
}

// Create a horizontal bar chart with a dropdown menu to display the top 10 OTUs found in that individual.
// Use sample_values as the values for the bar chart.
// Use otu_ids as the labels for the bar chart.
// Use otu_labels as the hovertext for the chart.

// Create a bubble chart that displays each sample.
// Use otu_ids for the x values.
// Use sample_values for the y values.
// Use sample_values for the marker size.
// Use otu_ids for the marker colors.
// Use otu_labels for the text values.

function createGraphs(selection) {
    var path = "static/data/samples.json"
    d3.json(path).then(function(d) {
        var jsondata = d["samples"];
        var selectedData = jsondata.filter(md => md.id == selection);
        // console.log(selectedData);
        var result = selectedData[0];

        var otuID = result["otu_ids"];
        var sampleValues = result["sample_values"];
        var otuLabels = result["otu_labels"];
        console.log(jsondata);

        var topSamples = otuID.slice(0,10).reverse();
        var topSampleValues = sampleValues.slice(0,10).reverse();
        var topLabels = otuLabels.slice(0,10).reverse();

        var barTrace = {
            x:topSampleValues,
            y:topSamples,
            text:topLabels,
            marker:{
                color: "#90d2d8"
            },
            type: "bar",
            orientation: "h"
        };

        var barLay = {
            title: "Top 10 OTU"
        };

        var bubbleTrace = {
            x:otuID,
            y:sampleValues,
            text:otuLabels,
            mode: "markers",
            marker:{
                size: sampleValues,
                color: otuID,
                colorscale: "Rainbow",
                type: "scatter",
                opacity: 0.4
            }
        };

        var bubblay = {
            title: "Values Per OTU ID",
            xaxis: {title: "OTU ID"},
            showlegend: true,
            hovermode: "closest"
        };

        Plotly.newPlot("bar", [barTrace], barLay);
        Plotly.newPlot("bubble", [bubbleTrace], bubblay);
    });
}

function initSample() {
    var selectdata = d3.select("#selDataset");
    var path = "static/data/samples.json"

    d3.json(path).then(function(d) {
        var sampName = d.names;

        sampName.forEach(function(s) {
            selectdata.append("option").text(s).property("value")
        });
        getJSON(sampName[0]);
        createGraphs(sampName[0]);
    });
}

function optionChanged(s) {
    getJSON(s);
    createGraphs(s);
}

initSample();
