$(function (){
    let result = $("#resultCode").val();
    if(result == "0"){
        alert("User name or password does not match!");
        $("#rateList").attr("action","/rate/detail/");
        $("#rateList").submit();
    }else if(result=="1"){
        alert("정상 적으로 삭제 되었습니다.");
        $("#rateList").attr("action","/rate/list/");
        $("#rateList").submit();
    }else if(result == "2"){
        alert("정상 적으로 등록 되었습니다.");
        $("#rateList").attr("action","/rate/list/");
        $("#rateList").submit();
    }
    else if(result == "4"){
        alert("정상 적으로 수정 되었습니다.");
        $("#rateList").attr("action","/rate/list/");
        $("#rateList").submit();
    }
    else if(result == "5"){
        alert("사용자 이름 또는 패스워드가 일치하지 않습니다!");
        $("#rateList").attr("action","/rate/detail/");
        $("#rateList").submit();
    }
    else if(result == "6"){
        alert("학교 인증 패스워드가 일치하지 않습니다!");
        $("#rateList").attr("action","/rate/write/");
        $("#rateList").submit();
    }
});