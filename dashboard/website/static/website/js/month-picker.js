/*
 * RV Metron - Month only Datepicker
 *
 * Requires : bootstrap-datepicker.min.js
 *
 *  HOW TO USE:
 *
 *
52             <div class="form-group" id="datepicker-container">
53                 <label for="datepicker_div">Selecione o mês:</label
54                 <div id="datepicker_div"></div>
55                 {% for error in goals_form.errors %}
56                     {% if "goal_initial" in error %}
57                         <span id="span-datapicker" class="help-block has-error" >
58                     {% endif %}
59                 {% endfor %}
60             </div>
 *
122     <script language="JavaScript">
123         var container = '#datepicker-container div'
124         var span = '#span-datapicker'
125         var input = '#id_goal_initial'
126         $(monthPicker(container, span, input));
127     </script>
 *
 *
*/

// Based on:
// http://eternicode.github.io/bootstrap-datepicker/

function monthPicker(mp_container, mp_span, mp_input){
    $(mp_container).datepicker({
        format: "dd/mm/yy",
        //clearBtn: true,
        language: "pt-BR",
        orientation: "bottom auto",
        autoclose: true,
        todayHighlight: true,
        format: "mm-yyyy",
        viewMode: "months",
        minViewMode: "months"
    }).on('changeMonth', function(ev){
        //console.log(ev); // DEBUG
        var currMonth = new Date(ev.date).getMonth()+1;
        var currYear = String(ev.date).split(" ")[3];
        var currData = currYear + "-" + currMonth + "-1"
        //console.log(data);
        $(mp_span).attr('style', 'display:none');
        $(mp_input).attr('value', currData);
    });;
}
