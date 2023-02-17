$(function (){
    $(".itemSelected").on('dblclick', 'td', function () {
        location.href="/rate/detail/" + $(this).parent().parent().children('input').val()
    });
});

