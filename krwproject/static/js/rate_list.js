$(function (){
    $(".itemSelected").on('dblclick', 'td', function () {
        location.href="/rate/detail/" + $(this).parent().parent().children('input').val()
    });

    $('#writeData').click(function (){
        location.href = "/rate/write/";
    });

    $('#goHome').click(function (){
        location.href = "/";
    });
});

