//
// pokertool.js
// @author: Brian
//


function pokerHand(){
  var handprogres = document.getElementById("handprogres");
  var handresults = document.getElementById("handresults");
  var logs = document.getElementById("logs");
  var cardx1 = document.getElementById("cardx1");
  var cardx2 = document.getElementById("cardx2");
  var cardx3 = document.getElementById("cardx3");
  var cardx4 = document.getElementById("cardx4");
  var cardx5 = document.getElementById("cardx5");
  var csrft = document.getElementById("csrft");
  var csrf_token = document.querySelector('[name=csrfmiddlewaretoken]');
  var tokens = {'csrft': csrft.value, 'csrf_token': csrf_token.value};
  console.log({'tokens': tokens});

  handprogres.value += 5;
  var results = 0;
  var logsX = [];
  handresults.innerHTML = results;
  logs.innerHTML = results;
  var url1 = window.location.href;
  var url22 = url1+"pokerhandTool";
  var url2 = "/pokerhandapp/pokerhand";
  console.log("url1: "+url1);
  console.log("url22: "+url22);
  console.log("url2: "+url2);
  var dy = new Date();
  var db = fetch(url2, {
      method: 'POST',
      body: JSON.stringify({
        card01: cardx1.value,
        card02: cardx2.value,
        card03: cardx3.value,
        card04: cardx4.value,
        card05: cardx5.value,
        csrfmiddlewaretoken: csrft.value
      }),
      headers: {'X-CSRFToken': csrft.value,
        'Content-type':'application/json; charset=UTF-8'
      },
      //mode: 'same-origin'
    }).then((response) => {
    console.log("db: ", db);
    console.log("response: ", response);
    handprogres.value += 5;
    logsX[++results] = response;
    handresults.innerHTML = response;
    return response.text();
  }).then((dblist) => {
    logsX[++results] = dblist;
    console.log('text(): ', dblist);
    var d1 = JSON.stringify(dblist);
    var db2 = JSON.parse(dblist);
    console.log("d1: ", d1);
    console.log("db2: ", db2);
    handprogres.value += 5;
    handresults.innerHTML = d1;
    logs.innerHTML = d1
    logsX[++results] = d1;
    logsX[++results] = db2;
    return db2;
  }).catch((error) => {
    logsX[++results] = error;
    console.log("Erros: ", error);
    handprogres.value = 3;
  }).finally(() => {
    var d2 = new Date();
    var d3 = d2 - dy;
    console.log(d2+"# db4: ", db,", @"+d3);
    handprogres.value = 70;
    logsX[++results] = d3;
  });
  console.log('logs: ', logsX);
}
