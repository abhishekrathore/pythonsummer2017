var a = 5;
title = document.getElementById("title");
input = document.getElementById("i");
select = document.getElementById("sel");



function getValue(){
    title.innerText = input.value;
}

function setValue(){
    input.value = select.value;
}
