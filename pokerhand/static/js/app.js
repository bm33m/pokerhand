//
// app.js
// @author: Brian
//
var cards = [];
var i = 0;
var max = 5;

function cardsInfo(table){
  var tableName = document.getElementById(table);
  var name = table.trim();
  var info1 = "info1";
  var cardXY = "cardXY";
  var j = 0;
  if (i >= max){
    alert(i+" >= "+max+" "+cards);
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
  return name;
}
