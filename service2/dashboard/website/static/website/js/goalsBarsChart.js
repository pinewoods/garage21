/*
    TUTORIAL:

    1) define this vars:

    var sabesp_goal = [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0];
    var pinewoods_goal = [12.0, 12.0, 12.0, 11.0, 11.0, 11.0, 10.0, 10.0, 10.0, 9.0, 9.0, 9.0];
    var sabesp_sample = [7.9, 8.6, 9.5, 8.4, 12.5, 11.0, 8.6, 7.9, 9.3, 9.0, 10.9, 12.0];
    var pinewoods_sample = [9.3, 8.2, 7.5, 8.5, 10.9, 10.5, 8.0, 9.6, 9.0, 10.3, 9.6, 11.4];
    // goals_chart_selector = '#goals_chart_div';
*/

function getSabespGoal(goal)
{
    var listGoal = [];

    for (var i = 0; i < 12; i++) {
        listGoal.push(goal);
    }
    return listGoal;
}
function removeDate(data, property)
{
    var list = [];

    for (var i = 0; i < data.length; i++) {
        list.push(data[i][property]); 
    }
    return list;
}

function goalsBarChart(goals_chart_selector,services) {

    var sabesp_goal = [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0];
    var pinewoods_goal = [12.0, 12.0, 12.0, 11.0, 11.0, 11.0, 10.0, 10.0, 10.0, 9.0, 9.0, 9.0];
    var sabesp_sample = [7.9, 8.6, 9.5, 8.4, 12.5, 11.0, 8.6, 7.9, 9.3, 9.0, 10.9, 12.0];
    var pinewoods_sample = [9.3, 8.2, 7.5, 8.5, 10.9, 10.5, 8.0, 9.6, 9.0, 10.3, 9.6, 11.4];

    
    $(goals_chart_selector).highcharts({
        credits: {
            enabled: false
        },
        exporting: {
             enabled: false
        },
        chart: {
            zoomType: 'xy'
        },
        title: {
            text: '',
        },
        xAxis: {
            categories: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun',
                'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dec'],
            crosshair: true
        },
        yAxis: {
            title: {
                text: 'Consumo em Metros Cúbicos (M³)'
            },
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }]
        },
        tooltip: {
            shared: true
        },
        /*
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'middle',
            borderWidth: 0
        },
        */
        legend: {
            layout: 'vertical',
            enabled: true,
            floating: true,
            verticalAlign: 'bottom',
            align: 'left',
            y:-30,
            x: 85,
            backgroundColor: '#FFFFFF' 
        },
        series: [{
            name: 'Meta Sabesp',
            color: '#00A5FF',
            type: 'spline',
            zIndex: 4,
            marker: {
                enabled: false
            },
        }, {
            name: 'Meta Wolksen',
            color: '#FF9933',
            type: 'spline',
            zIndex: 3,
            marker: {
                enabled: false
            },
        }, {
            name: 'Leitura Sabesp',
            color: '#6699CC',
            type: 'column',
            zIndex: 2
        }, {
            name: 'Leitura Wolksen',
            color: '#66CC99',
            type: 'column',
            zIndex: 1
        }]
    });
    
    $.getJSON(services[0],function(data){
        goals = getSabespGoal(data.results[0].consumption_goal);
        $("#goals_chart_div").highcharts().series[0].setData(goals);
    });
    $.getJSON(services[1],function(data){
        $("#goals_chart_div").highcharts().series[1].setData(removeDate(data.results, "goal"));
    });
    $.getJSON(services[2],function(data){
        $("#goals_chart_div").highcharts().series[2].setData(removeDate(data.results, "reading_m3"));
    });
    $.getJSON(services[3],function(data){
        $("#goals_chart_div").highcharts().series[3].setData(data.sensor_reading);
    });
}