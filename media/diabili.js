/*
Autor : Fadiga Ibrahima
Soft: Zozaniba

*/

function dabili_init() {

    addJQ_ask_list();
    refresh_nbr();
    // var pe = new PeriodicalExecuter();
    // pe.initialize(declencherTraitements, 10);

}

function addJQ_ask_list() {
    $.getJSON('/diabili/getask', function(data) {
        $.each(data.asks, function(num, ask) {
            row = "<li class='mess" + ask.id+"'"+">" + "De " + ask.num_phone  + ' a (' + ask.date +') ' +
                  "</li>" + "<li><a href='#' ask-id=" + ask.id + ">" + ask.question + "</a></li>";
            $("#ask_list").append(row);
        });
    add_JQ_();
    });

}

function add_JQ_() {
    $("#ask_list li a").click(function() {
        var ask_id = $(this).attr('ask-id');
        // var ask_name = $(this).("#ask-id").attr();
        $("#ask-amswer").html(ask_id);
        $(".mess" + ask_id).remove();
        $(this).remove();
    });
}

function declencherTraitements() {
    alert("10");
}


function search_in_google(){
     // var ask = $(this).attr('search-google');
     // google.load("search", ask)

    google.load('search', '1');
    google.setOnLoadCallback(function(){
      new google.search.CustomSearchControl().draw('cse');
    }, true);
}

function get_JQ_addressbook_new_group() {
    $("#add_group_btn").click(function() {
        group_name =  $("#id_reponse").val();
        $("#id_reponse").val("");
        $.post('diabili/answer/'+group_name, function(data) {
            display_alert(data.return, data.return_html, 2);
            // refresh_group_list();
        }, "json");
    });
    refresh_nbr();
}

function refresh_nbr() {
    $.getJSON('/diabili/getask', function(data){
        $("#nbr_inbox").html(data.nbr_inbox);
        $("#nbr_send").html(data.nbr_send);
    });
}