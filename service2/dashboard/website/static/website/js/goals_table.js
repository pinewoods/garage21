/*

    Two parameters must be defined !!!

    in order to use:
    - built_paginator
    - built_table

    // Marks the active page on paginator
    var activePage = 1;
    // Paginator link
    var base_url = "{% url 'goals-list' %}?page="

 * */

function built_paginator(data){
    // Reset inner HTML
    $('#ul_paginator').empty();
    // Creates the <<
    if(data.previous){
        $("#ul_paginator").append(
        '<li class="previous"><a href="'+data.previous+'">&larr;</a></li>');
    }else{
        $("#ul_paginator").append(
        '<li class="previous disabled"><a href="#">&larr;</a></li>');
    }

    //n_pages = Math.ceil(data.count / data.results.length);
    //Number of results.length == 1 sometimes
    n_pages = Math.ceil(data.count / 10);
    console.log(activePage);
    for(i=1; i<=n_pages; i++){
        console.log(activePage, i, activePage==i);
        if(activePage==i){
            li_elem = '<li class="active"><a href="'+base_url+i+'">'+i+'</a></li>';
        }else{
            li_elem = '<li><a href="'+base_url+i+'">'+i+'</a></li>';
        }
        $("#ul_paginator").append(li_elem);
    }

    // Creates the >>
    if(data.next){
        $("#ul_paginator").append(
        '<li class="next"><a href="'+data.next+'">&rarr;</a></li>');
    }else{
        $("#ul_paginator").append(
        '<li class="next disabled"><a href="#">&rarr;</a></li>');
    }
};

//TODO Rounding
function built_table(data){
    // Reset inner HTML
    $('#records_tboby').empty();
    $.each(data.results, function(i, item) {

        // Colors the table
        tr_obj = '<tr>';
        if((item.goal*0.9) > item.real_consume){
            tr_obj = '<tr class="success">';
        }
        if(item.real_consume > (item.goal*1.1)){
            tr_obj = '<tr class="warning">';
        }
        if(item.real_consume > (item.goal*1.2)){
            tr_obj = '<tr class="danger">';
        }

        // Fill data
        $(tr_obj).append(
            $('<th scope="row">').text(item.end_date),
            $('<td>').text(item.goal),
            $('<td>').text(item.est_consume),
            $('<td>').text(item.real_consume)
        ).appendTo('#records_tboby')
    });
};
