$(function (){
    let result = $("#resultCode").val();
    if(result == "0"){
        alert("사용자 이름 또는 패스워드가 일치하지 않습니다!");
        location.href="/rate/detail/" + $("#ratecontentId").val();
    }else if(result=="1"){
        alert("정상적으로 삭제 되었습니다.");
         location.href="/rate/list/";
    }else if(result == "2"){
        alert("정상적으로 등록 되었습니다.");
         location.href="/rate/list/";
    }
});