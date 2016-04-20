// http://jsfiddle.net/nate439j/4/

function sparkline_timeseries(div_selector, data_points) {
    $(div_selector).highcharts({
        credits: {
            enabled: false
        },

        exporting: {
            enabled: false
        },

        title: {
            text: ''
        },
        
        chart:{
            renderTo: 'container',
            margin:[0, 0, 0, 0],
            backgroundColor:'transparent'
        },
        
        xAxis: {
            labels:{
                enabled:false
            }
        },
        legend:{
            enabled:false
        },
        yAxis: {
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
        tooltip: {
          formatter: function() {
            return  Highcharts.dateFormat('%H:%m (%d/%b)', new Date(this.x*1000)) + ': <b>' + this.y + ' %</b>';
          }
        },
        series : [{
            type: 'area',
            color: '#6DA398',
            data : data_points,
            tooltip: {
                valueDecimals: 0,
                valueSuffix: '%'
            },
            threshold: null,
             marker:{
                    //enabled:false,
                    radius:0,
                    states:{
                        hover:{
                            radius:2
                        }
                    }
                }
        }]
    });
}

mydata = [
	[1461148998, 50],
  [1461159020, 75],
  [1461169080, 65],
 	[1461178998, 50],
  [1461189020, 75],
  [1461199080, 65]
]

$(sparkline_timeseries('#container', mydata));
