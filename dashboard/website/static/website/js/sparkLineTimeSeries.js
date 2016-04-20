function sparkline_timeseries(div_selector, data_points) {

    $(div_selector).highcharts({
        credits: {
            enabled: false
        },

        /*
        chart:{
            //renderTo: div_selector,
            margin:[0, 0, 0, 0],
            backgroundColor:'transparent'
        },
        */

        exporting: {
            enabled: false
        },


        title: {
            text: ''
        },

        xAxis: {
            //gapGridLineWidth: 0,
            labels:{
                enabled:false
            }
        },

        yAxis:{
            min: 0,
            max: 101,
            maxPadding:0,
            minPadding:0,
            gridLineWidth: 0,
            endOnTick:false,
            labels:{
                enabled:false
            }
        },

        legend: {
            enabled: false
        },

        tooltip: {
            enabled: true
        },

        plotOptions: {
            series: {
                enableMouseTracking: true,
                lineWidth: 1,
                shadow: false,
                states: {
                    hover: {
                        lineWidth: 1
                    }
                },
                marker: {
                    //enabled:false,
                    radius: 0,
                    states: {
                        hover: {
                        radius: 2
                        }
                    }
                }
            }
        },

        series : [{
            //name : 'Nível',
            type: 'area',
            data : data_points,
            gapSize: 5,
            tooltip: {
                valueDecimals: 0,
                valueSuffix: '%'
            },
            threshold: null
        }]
    });
}
