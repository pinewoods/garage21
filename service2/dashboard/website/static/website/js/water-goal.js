function water_goal_graph(meta, consumo){

$(function () {
    $('#container').highcharts({
        title: {
            text: 'Meta de Consumo de Água',
            x: -20 //center
        },
        subtitle: {
            text: 'Consolidado Mensal',
            x: -20
        },
        xAxis: {
            categories: ['1', '2', '3', '4', '5',
                '6','7', '8', '9', '10', '11', '12',
                '13', '14', '15', '16', '17', '18',
                '19', '20', '21', '22', '23', '24',
                '25', '26', '27', '28', '29', '30']
        },
        yAxis: {
            title: {
                text: 'Volume de Água (L)'
            },
            min:0,
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }]
        },
        tooltip: {
            valueSuffix: ' L'
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'middle',
            borderWidth: 0
        },
        series: [{
            name: 'Meta',
            data: [7.0, 6.9, 9.5, 14.5]
        }, {
            name: 'Consumido',
            data: [0.8, 5.7, 11.3, 17.0, 22.0, 24.8, 24.1, 20.1, 14.1, 8.6, 2.5]
        }]
    });
        var data = new Date(new Date().getFullYear(),new Date().getMonth() + 1, 1);
        data.setDate(0);
        days = data.getDate();
        
        $('#container').highcharts().series[0].setData(meta);
        $('#container').highcharts().series[1].setData(consumo);
        $('#container').highcharts().xAxis[0].setExtremes(0,days);
});

}