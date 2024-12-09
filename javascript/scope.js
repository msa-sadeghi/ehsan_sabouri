// let myVariable = 23;
// function myFunction() {
//   console.log("first one", myVariable);
// }

// myFunction();
// console.log("second one", window.myVariable);

// {
//   let x = 22;
// }
// console.log("third one", x);

// myFunction2();

// function myFunction2() {
//   console.log("hello");
// }
// console.log(x);
// var x = 22;

// let x = 12;
// let x = 13;
// console.log(x);
// "use strict";
// var x = 12;
// console.log(x);

// function myFunction(y, y) {}
let myElement = document.getElementsByTagName("div")[0];

function getTime() {
  let date = new Date();
  var hour = date.getHours();
  var minutes = date.getMinutes();
  var seconds = date.getSeconds();
  console.log(hour + ":" + minutes + ":" + seconds);
  myElement.innerHTML = hour + ":" + minutes + ":" + seconds;
  document.body.style = "display:flex; justify-content:center; ";
  myElement.style = "font-size:32px; color:red";
}

setInterval(getTime, 1000);
