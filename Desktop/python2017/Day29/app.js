var a = 5;
function doSearch(){

 $("#name").html("");
var search = $("#search").val();
var base_url = "https://gateway.marvel.com"
var path = "/v1/public/characters?apikey=1f1eef6169fc3b523d81a6983f7e14f2&limit=100&nameStartsWith="+search
$.ajax({
  url: base_url+path,
  dataType: 'json',
  success: function(data) {
    console.log(data);  

    var superheros = data.data.results;

    for(var i=0;i<superheros.length;i++){
                   
         $("#name").append("<p>"+superheros[i].name+
         "</p><img src='"+superheros[i].thumbnail.path+"."
         +superheros[i].thumbnail.extension+"'>")


    }

   
       // $("#photo").attr("src",url)

  }
});


}

// var base_url = "https://randomuser.me"
// var path = "/api"
// $.ajax({
//   url: base_url+path,
//   dataType: 'json',
//   success: function(data) {
//     console.log(data);  
//     var first = data.results[0].name.first;
//     var last = data.results[0].name.last;
//     var title = data.results[0].name.title;
//     var url = data.results[0].picture.large;

//         $("#name").text(title+" "+first+" "+last)
//         $("#photo").attr("src",url)



//   }
// });