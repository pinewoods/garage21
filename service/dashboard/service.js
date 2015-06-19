  var graph = new Array();

            $(function () {
                $('#container').highcharts({
                    chart: {
                        zoomType: 'x'
                    },
                    title: {
                        text: 'Quantidade de Água disponível ao longo do Tempo'
                    },
                    subtitle: {
                        text: document.ontouchstart === undefined ?
                            'Click and drag in the plot area to zoom in' :
                            'Pinch the chart to zoom in'
                    },
                    xAxis: {
                        type: 'datetime',
                        minRange: 14 * 24 * 3600000 // fourteen days
                    },
                    yAxis: {
                        title: {
                            text: 'Nível da Caixa'
                        }
                    },
                    legend: {
                        enabled: false
                    },
                    plotOptions: {
                        area: {
                            fillColor: {
                                linearGradient: {
                                    x1: 0,
                                    y1: 0,
                                    x2: 0,
                                    y2: 1
                                },
                                stops: [
                                    [0, Highcharts.getOptions().colors[0]],
                                    [1, Highcharts.Color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
                                ]
                            },
                            marker: {
                                radius: 2
                            },
                            lineWidth: 1,
                            states: {
                                hover: {
                                    lineWidth: 1
                                }
                            },
                            threshold: null
                        }
                    },
                    series: [{
                        type: 'area',
                        name: "Nível D'agua",
                        pointInterval: 24 * 3600 * 1000,
                        pointStart: Date.UTC(2015, 0, 1),
                        data: []
                    }]
                });

                $.getJSON("http://ws.pinewoods.com.br/api", function(data){ 

                    $.each(data, function(i, item){
                            graph.push(item.reading);
                    });
                    $('#container').highcharts().series[0].setData(graph);
                });

            });