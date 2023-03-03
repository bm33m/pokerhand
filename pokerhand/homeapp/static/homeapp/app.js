//
// app.js
// @author: Brian
//

function cardsInfo(table){
  var tableName = document.getElementById(table);
  var name = table.trim();
  var name2 = name.split("&#x27;")
  console.log("cardsInfo: ", name2);
  tableName.value = name;
  return name;
}
