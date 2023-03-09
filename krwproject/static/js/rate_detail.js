$(function (){
    $('#goList').click(function (){
        $('#rateList').attr('action',"/rate/list/");
        $('#rateList').submit();
    });

     $('#deleteData').click(function (){
        if($('#contentData #userId').val().trim()==""){
              alert("Please enter your name");
             return;
         }

         if($('#contentData #userpwd').val().trim()==""){
              alert("Please enter your password!");
             return;
         }
         var rlt = confirm('Are you sure you want to delete ?');
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
             alert("Select at least 3 stars!");
             return;
         }

         if($('#contentData #content').val().trim()==""){
              alert("Please enter your fill-in!");
             return;
         }

         if($('#contentData #userId').val().trim()==""){
              alert("Please enter your name!");
             return;
         }

         if($('#contentData #userpwd').val().trim()==""){
              alert("Please enter your password!");
             return;
         }

         var rlt = confirm('Are you sure you want to update?');
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
