var a = 5;
title = $("#title");
input = $("#i");
select = $("#sel");


function getValue(){
    title.text(input.val())
}

function setValue(){
    input.val(select.val());
}

function changeColor(){
    var c = $("#title").attr("class");
    console.log(c);
    if(c){
      $("#title").attr("class","");
    }else{
      $("#title").attr("class","style1");

    }

   var p = $("#title").css("padding-left");
   console.log(p);


   setTimeout(changeColor, 100)

    $("#title").css("padding-left",parseInt(p)+5)
}


function addComment(){
    text = $("#i").val()
    $("#div1").append("<p> "+text+" </p>")
}



// $(), .text(), .val(), .attr(), .html(), .css(), .append()