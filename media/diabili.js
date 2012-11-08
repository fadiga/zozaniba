/*
Autor : Fadiga Ibrahima
Soft: Zozaniba

*/

function dabili_init() {

    addJQ_ask_list();
    refresh_nbr();
    setInterval("refresh()", 5000); // Répète la fonction toutes les 50 sec

}

function addJQ_ask_list() {
    $.getJSON('/diabili/getask', function(data) {
        $.each(data.asks, function(num, ask) {
            row = "<li class='mess" + ask.id+"'"+">" + "De " + ask.num_phone  + ' a (' + ask.date +') ' +
                  "</li>" + "<li><a href='#' ask-id=" + ask.id + ">" + ask.question + "</a></li>";
            $("#ask_list").append(row);
        });
    add_JQ_();
    send_JQ_answer();
    });

}

function del_ask_list() {

    $("#ask_list").children('li').remove();

}

function add_JQ_() {
    $("#ask_list li a").click(function() {
        var ask_id = $(this).attr('ask-id');
        $("#ask-amswer").html(ask_id);
        $(".mess" + ask_id).remove();
        $(this).remove();
    });
}

function send_JQ_answer() {
    $("#send_btn").click(function() {
        answer =  $("#id_reponse").val();
        $("#id_reponse").val("");
        $.post('answer/' + answer, function(data) {
               display_alert(data.return, data.return_html, 2);
        }, "json");
    });
}

function refresh_nbr() {
    $.getJSON('/diabili/getask', function(data){
        $("#nbr_inbox").html(data.nbr_inbox);
        $("#nbr_send").html(data.nbr_send);
    });
}


function refresh() {
    refresh_nbr();
    del_ask_list();
    addJQ_ask_list();
}
