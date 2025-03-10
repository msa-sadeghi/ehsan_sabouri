"use strict";
// function myFunction() {
//   console.log(this);
// }

// myFunction();
let student = {
  esm: "reza",
  family: "rezaei",
  scores: [90, 50, 100, 78],
  walk: function () {
    console.log(`${this.esm} ${this.family} is walking`);
  },
  calcAve: function () {
    let sum = 0;
    // let myThis = this;
    this.scores.forEach(
      function (sc) {
        if (sc < 60) {
          sc += 10;
          // console.log(myThis.esm);
          console.log(this.esm);
        }
        sum += sc;
      }.bind(this)
    );
    console.log(sum / this.scores.length);
  },
};
student.walk();
student.calcAve();
