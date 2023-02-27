$(function (){
    $('#Search').click(function (){
        $("#rateList").attr("action","/rate/list/");

        $("#rateList #categoryId").val($("#category").val());
        $("#rateList #subcategoryId").val($("#subcategory").val());
        $("#rateList #sort").val($("input[name='sort']:checked").val());
        $("#rateList").submit();
    });

    Search

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

     $('#category').change(function (){
        if($('#category option:selected').val() == "empty"){
            $("select#subcategory option").remove();
            return;
        }

      $.get('/rate/get_subcategory/',
          {
              id: $('#category option:selected').val()
          },
          function(data, status){
             if(status == 'success') {
                 $("select#subcategory option").remove();
                  for(let i=0;i<data.length;i++){
                     $("select#subcategory").append("<option value='" + data[i].pk + "'>" + data[i].fields['subcategory_name'] + "</option>");
                  }
             }
         }
      );
    });

});

