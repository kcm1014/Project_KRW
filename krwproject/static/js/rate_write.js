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

  $(document).ready(function (){
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

    $('#writeData').click(function (){
        //카테고리 정보
        if($('#category option:selected').val() == "empty"){
            alert("카테고리를 선택하세요!");
            return;
        }

         if($('#subcategory option:selected').val() == ""){
            alert("서브 카테고리를 선택하세요!");
            return;
        }

         let count = 0;
         if($('#startpoint01').val()=='0') count++;
         if($('#startpoint02').val()=='0') count++;
         if($('#startpoint03').val()=='0') count++;
         if($('#startpoint04').val()=='0') count++;
         if($('#startpoint05').val()=='0') count++;
         if($('#startpoint06').val()=='0') count++;
         if(count > 3){
             alert("3개 이상의 별점을 선택하세요!");
             return;
         }

         if($('#content').val().trim()==""){
              alert("작성 내용을 입력하세요!");
             return;
         }

         if($('#userId').val().trim()==""){
              alert("작성자 이름을 입력하세요!");
             return;
         }

         if($('#userpwd').val().trim()==""){
              alert("패스워드를 입력하세요!");
             return;
         }

         if($('#schPwd').val().trim()==""){
              alert("학교 인증 패스워드를 입력하세요!");
             return;
         }
        if($('#chkPwd').val().trim()=="notExist"){
            alert("학교 인증 패스워드가 발급되지 않은 상태입니다");
             return;
        }
         if($('#schPwd').val().trim()!=$('#chkPwd').val().trim()){
              alert("학교 인증 패스워드가 일치 하지 않습니다!");
             return;
         }


         var rlt = confirm('등록하시겠습니까?');
         if(rlt) {
             $('#dataWrite').submit();
         }
    });

    $('#goList').click(function (){
        $("#rateList").attr("action","/rate/list/");
        $("#rateList").submit();
    });

  });
