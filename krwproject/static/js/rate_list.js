$(function (){
    $(".itemSelected").on('dblclick', 'td', function () {
        $("#pk").val($(this).parent().parent().children('input').val());
        $('#rateList').attr("action","/rate/detail/");
        $('#rateList').submit();
        //location.href="/rate/detail/" + $(this).parent().parent().children('input').val()
    });

    $('#writeData').click(function (){
        $("#rateList").attr("action","/rate/write/");
        $("#rateList").submit();
    });

    $('#goHome').click(function (){
        location.href = "/";
    });

    $('#pageNumber li').click(function (){
        $("#currentPage").val($(this).val());
        $('#rateList').submit();
    });

});

