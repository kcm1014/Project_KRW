$(function (){
    let result = $("#resultCode").val();
    if(result == "0"){
        alert("User name or password does not match!");
        $("#rateList").attr("action","/rate/detail/");
        $("#rateList").submit();
    }else if(result=="1"){
        alert("Done!");
        $("#rateList").attr("action","/rate/list/");
        $("#rateList").submit();
    }else if(result == "2"){
        alert("Done!");
        $("#rateList").attr("action","/rate/list/");
        $("#rateList").submit();
    }
    else if(result == "4"){
        alert("Done!");
        $("#rateList").attr("action","/rate/list/");
        $("#rateList").submit();
    }
    else if(result == "5"){
        alert("User name or password does not match!");
        $("#rateList").attr("action","/rate/detail/");
        $("#rateList").submit();
    }
    else if(result == "6"){
        alert("School authentication passwords do not match!");
        $("#rateList").attr("action","/rate/write/");
        $("#rateList").submit();
    }
});
