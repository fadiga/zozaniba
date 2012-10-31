/*
Autor : Fadiga Ibrahima
Soft: Zozaniba

*/

function dabili_init() {
    addJQ_ask_list();
    // var pe = new PeriodicalExecuter();
    // pe.initialize(declencherTraitements, 10);

}

function addJQ_ask_list() {
    $.getJSON('/diabili/getask', function(data) {
        $.each(data.asks, function(num, ask) {
            row = "<li>" + "De " + ask.num_phone  + ' a (' + ask.date +') ' + "</li>" + "<li><a href='#' ask-id=" + ask.id + ">" + ask.question + "</a></li>";
            $("#ask_list").append(row);
        });
    add_JQ_();
    });

}

function add_JQ_() {
    $("#ask_list li a").click(function() {
        var ask_id = $(this).attr('ask-id');
        $("#ask-amswer").html(ask_id);
        $(this).parent().remove();
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
