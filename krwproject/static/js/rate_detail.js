$(function (){
    $('#goList').click(function (){
        $('#rateList').attr('action',"/rate/list/");
        $('#rateList').submit();
    });

     $('#deleteData').click(function (){
        if($('#contentData #userId').val().trim()==""){
              alert("작성자 이름을 입력하세요!");
             return;
         }

         if($('#contentData #userpwd').val().trim()==""){
              alert("패스워드를 입력하세요!");
             return;
         }
         var rlt = confirm('삭제하시겠습니까?');
         if(rlt){
             $('#rateList').attr('action',"/rate/delete/");
             $("#rateList #pk").val($("#contentData #pk").val());
             $("#rateList #userId").val($("#contentData #userId").val());
             $("#rateList #userpwd").val($("#contentData #userpwd").val());

             $('#rateList').submit();
         }

    });

     $('#updateData').click(function (){
         let count = 0;
         if($('#contentData #startpoint01').val()=='0') count++;
         if($('#contentData #startpoint02').val()=='0') count++;
         if($('#contentData #startpoint03').val()=='0') count++;
         if($('#contentData #startpoint04').val()=='0') count++;
         if($('#contentData #startpoint05').val()=='0') count++;
         if($('#contentData #startpoint06').val()=='0') count++;
         if(count > 3){
             alert("3개 이상의 별점을 선택하세요!");
             return;
         }

         if($('#contentData #content').val().trim()==""){
              alert("작성 내용을 입력하세요!");
             return;
         }

         if($('#contentData #userId').val().trim()==""){
              alert("작성자 이름을 입력하세요!");
             return;
         }

         if($('#contentData #userpwd').val().trim()==""){
              alert("패스워드를 입력하세요!");
             return;
         }

         var rlt = confirm('수정하시겠습니까?');
         if(rlt){
             $('#contentData').submit();
         }
    });
});


const drawStar01 = (target) => {
    document.querySelector(`.star #satr01`).style.width = `${target.value * 20}%`;
  }

  const drawStar02 = (target) => {
    document.querySelector(`.star #satr02`).style.width = `${target.value * 20}%`;
  }

  const drawStar03 = (target) => {
    document.querySelector(`.star #satr03`).style.width = `${target.value * 20}%`;
  }

  const drawStar04 = (target) => {
    document.querySelector(`.star #satr04`).style.width = `${target.value * 20}%`;
  }


  const drawStar05 = (target) => {
    document.querySelector(`.star #satr05`).style.width = `${target.value * 20}%`;
  }


  const drawStar06 = (target) => {
    document.querySelector(`.star #satr06`).style.width = `${target.value * 20}%`;
  }