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
            alert("Select a category!");
            return;
        }

         if($('#subcategory option:selected').val() == ""){
            alert("Select a subcategoory");
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
             alert("Select a least 3 stars!");
             return;
         }

         if($('#content').val().trim()==""){
              alert("Please Enter yoour fill-in!");
             return;
         }

         if($('#userId').val().trim()==""){
              alert("Please enter your name");
             return;
         }

         if($('#userpwd').val().trim()==""){
              alert("Please enter your password!");
             return;
         }

         if($('#schPwd').val().trim()==""){
              alert("Enter your school authentication password!");
             return;
         }
        if($('#chkPwd').val().trim()=="notExist"){
            alert("School authentication password has noot been issued");
             return;
        }
         if($('#schPwd').val().trim()!=$('#chkPwd').val().trim()){
              alert("Shcool authentication passwords do not match!");
             return;
         }


         var rlt = confirm('Are you sure want to upload?');
         if(rlt) {
             $('#dataWrite').submit();
         }
    });

    $('#goList').click(function (){
        $("#rateList").attr("action","/rate/list/");
        $("#rateList").submit();
    });

  });
