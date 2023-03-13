//
// app.js
// @author: Brian
//
var cards = [];
var i = 0;
var max = 5;
var handX = 0;
var hand = [];

function cardsInfo(table){
  var tableName = document.getElementById(table);
  var name = table.trim();
  var info1 = "info1";
  var cardXY = "cardXY";
  var j = 0;
  if (i >= max){
    //alert(i+" >= "+max+" "+cards);
    console.log(i+" >= "+max+" \n"+cards);
  } else {
    j = i + 1;
    cardXY = 'card0'+j
    info1 = document.getElementById(cardXY);
    info1.value = name;
  }
  //var name2 = name.split("&#x27;")
  //console.log("cardsInfo: ", name2);
  console.log(i+" cardsInfo: ", name);
  cards[i] = name;
  i++;
  tableName.value = name;
  hand[handX] = name;
  handX++;
  if(handX == 5) {
    getResults(hand);
    handX = 0;
    hand = [];
  }
  return name;
}


function getResults(hand){
  var log = document.getElementById("log");
  var logs = document.getElementById("logs");
  var url1 = window.location.href;
  console.log('url1: ',url1);
  var pokerhand = "/pokerhandapp/pokerhand?cards="+hand[0]+","+hand[1]+","+hand[2]+","+hand[3]+","+hand[4]+",getResults";
  console.log('url pokerhand: ', pokerhand);
  var dy = new Date();
  log.innerHTML = dy+"<br>Hand: <br>"+hand+"<br><br>Results: <br><br>";
  var db = fetch(pokerhand, {
      method: 'GET',
      headers: {'Content-type':'application/json; charset=UTF-8'}
    }).then((response) => {
    console.log("response: ", response);
    return response.text();
  }).then((dblist) => {
    var d1 = JSON.stringify(dblist);
    var db2 = JSON.parse(dblist);
    console.log("db1: ", d1);
    console.log("db2: ", db2);
    logs.innerHTML = d1
    return db2;
  }).catch((error) => {
    console.log("error: ", error);
  }).finally(() => {
    var d2 = new Date();
    var d3 = d2 - dy;
    console.log(d2+"# ", db,", @"+d3);
  });

}
