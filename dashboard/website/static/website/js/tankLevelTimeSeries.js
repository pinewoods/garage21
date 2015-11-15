function plot_level_timeseries(div_selector, data_points) {

    $(div_selector).highcharts('StockChart', {
        credits: {
            enabled: false
        },

        exporting: {
            enabled: false
        },

        title: {
            text: ''
        },

        xAxis: {
            gapGridLineWidth: 0
        },

        yAxis: {
            min: 0,
            max: 101
        },

        rangeSelector : {
            enabled:false,
        },

        /* TODO: Please Enable this in future !!! */
        navigator:{
            enabled:false,
        },

        series : [{
            name : 'Nível',
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
