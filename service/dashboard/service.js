var graph = new Array();


$(function () {
    $('#container').highcharts({
        chart: {
            type: 'spline'
        },
        title: {
            text: 'Disponibilidade de Água'
        },
        subtitle: {
            text: 'Quantidade disponível ao longo do Tempo'
        },
        xAxis: {
            type: 'datetime',
            dateTimeLabelFormats: { // don't display the dummy year
                month: '%e. %b',
                year: '%b'
            },
            title: {
                text: 'Período'
            }
        },
        yAxis: {
            title: {
                text: 'Nível do Reservatório'
            },
            min: 0
        },
        tooltip: {
            headerFormat: '<b>{series.name}</b><br>',
            pointFormat: '{point.x:%e. %b}: {point.y:.2f} m'
        },

        plotOptions: {
            spline: {
                marker: {
                    enabled: true
                }
            }
        },

        series: [{
            name: 'Volume',
            // Define the data points. All series have a dummy year
            // of 1970/71 in order to be compared on the same x axis. Note
            // that in JavaScript, months start at 0 for January, 1 for February etc.
            data: []
        }]
    });
    $.getJSON("http://ws.pinewoods.com.br/api", function(data){ 
        $.each(data, function(i, item){
                graph.push([item.timestamp,item.reading]);
        });
        $('#container').highcharts().series[0].setData(graph);
    });

});