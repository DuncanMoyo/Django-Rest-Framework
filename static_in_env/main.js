// Json - javascript object notation
// Ajax - asynchronous javascript and xml

var btn = document.getElementById("btn")
var container = document.getElementById("ourcontainer")
var url = 'http://127.0.0.1:8000/api'

//$.ajax({
//    method: 'GET',
//    url: url,
//    success: function(data){
//        console.log(data)
//        console.log("success")
//    },
//    error: function(error_data){
//        console.log("error")
//    }
//})


btn.addEventListener("click", function(){
    var ourRequest = new XMLHttpRequest();
    ourRequest.open("GET", url);
    ourRequest.onload = function(){
    console.log(ourRequest.responseText); //not json formatted
        var ourData = JSON.parse(ourRequest.responseText);
        console.log(ourData);
        renderHTML(ourData);
    }
    ourRequest.send();
})


function renderHTML(data){
    var container = document.getElementById("ourcontainer")
    var htmlString = "";

    for (i=0; i < data.length; i++){
        htmlString += "<p>This items's primary key is" + data[i].pk + "</p>";
    }
    container.insertAdjacentHTML('beforeend', htmlString);
}