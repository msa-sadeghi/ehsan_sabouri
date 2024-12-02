var persianKeys = {
  83: "س",
  68: "ی",
};

function keyDown(event) {
  console.log(event);
  if (event.keyCode in persianKeys) {
    event.preventDefault();
    event.target.value += persianKeys[event.keyCode];
  }
}

function change() {
  console.log("changed");
}

function clicked() {
  console.log("clicked");
  document.body.style.backgroundColor = "red";
}

function mouseOver(event) {
  console.log("mouse is overed!!");
  event.target.style.backgroundColor = "blue";
  event.target.style.color = "white";
  event.target.innerHTML = "hi";
}
function mouseOut(event) {
  console.log("mouse is out!!");
  event.target.style.backgroundColor = "brown";
  event.target.style.color = "white";
  event.target.innerHTML = "bye";
}
