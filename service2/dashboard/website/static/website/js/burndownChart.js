function burndownChart(selector, consumo, meta_sabesp, meta_pinewoods){

    $(function () {
        $(selector).highcharts({
            exporting: {
                enabled: false
            },
            title: {
                text: '',
            },
            xAxis: {
                categories: ['1', '2', '3', '4', '5',
                    '6','7', '8', '9', '10', '11', '12',
                    '13', '14', '15', '16', '17', '18',
                    '19', '20', '21', '22', '23', '24',
                    '25', '26', '27', '28', '29', '30', '31']
            },
            yAxis: {
                title: {
                    text: 'Volume de Água (M³)'
                },
                min:0,
                plotLines: [{
                    value: 0,
                    width: 1,
                    color: '#808080'
                }]
            },
            tooltip: {
                valueSuffix: ' M³',
                shared: true,
                valueDecimals: 2
            },
            legend: {
                //layout: 'vertical',
                enabled: true,
                floating: true,
                verticalAlign: 'bottom',
                align: 'left',
                y:-30,
                x: 45
            },
            credits: {
                enabled: false
            },
            series: [{
                name: 'Meta Sabesp',
                color: '#7CB5EC',
                data: meta_sabesp
            }, {
                name: 'Consumido',
                color: '#BA3C3D',
                data: consumo
            },
            {
                name: 'Meta Pinewoods',
                color: '#99CC33',
                data: meta_pinewoods
            }
        ]
        });

        var data = new Date(new Date().getFullYear(),new Date().getMonth() + 1, 1);
        data.setDate(0);
        days = data.getDate();

        $(selector).highcharts().xAxis[0].setExtremes(0,days);

    });
}
