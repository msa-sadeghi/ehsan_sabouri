// var allProducts = [
//   { id: 1, name: "laptop", price: 170 },
//   { id: 2, name: "phone", price: 60 },
//   { id: 3, name: "tablet", price: 80 },
//   { id: 4, name: "water", price: 5 },
//   { id: 5, name: "soft drink", price: 10 },
// ];

// var userBasket = [
//   { id: 1, name: "laptop", price: 170 },
//   { id: 2, name: "phone", price: 60 },
// ];

// var userRequest = prompt("1. Add Product\n 2. Remove product");
// if (userRequest === "1") {
//   var userProductName = prompt("Enter your name: ");
//   var productData;
//   var isInShop = allProducts.some(function (product) {
//     if (product.name === userProductName) {
//       productData = product;
//       return true;
//     }
//   });
//   if (isInShop === true) {
//     var newProduct = {
//       id: 3,
//       name: productData.name,
//       price: productData.price,
//     };
//     userBasket.push(newProduct);
//     console.log("Basket", userBasket);
//   } else {
//     console.log("not exists");
//   }
// } else if (userRequest === "2") {
//   var userProductName = prompt("Enter Your product name:");
//   var productIndex = userBasket.findIndex(function (product) {
//     return product.name === userProductName;
//   });
//   userBasket.splice(productIndex, 1);
//   console.log("Basket: ", userBasket);
// } else {
//   console.log("incorrect");
// }

// var scores = [2, 4, 5, 6, 7, 8, 9];
// var newScores = scores.map(function (score) {
//   return score ** 2;
// });

// console.log(newScores);

//  excersice

// یک پروژه فروشگاه آنلاین پیاده سازی کنید

// به این صورت که یک آرایه به عنوان سبد خرید کاربر در نظر بگیرید که 6 محصول به طور دیفالت دارد

// سیاست کاری فروشگاه به این شکل است که برای محصولاتی که بالای 100 هزار تومان باشند، از مشتری هزینه پست دریافت نمی شود

// اما محصولاتی که زیر 100 هزار تومان قیمت داشته باشند، برای هر کدام 1000 تومان هزینه ارسال (هزینه پست) دریافت میشه

// لطفا قیمت کل سبد خرید را همراه با هزینه پست محاسبه کرده و به کاربر نمایش دهید

// var userNames = ["Ali", "Sara", "Amir", "babak"];

// var filteredUserNames = userNames.filter(function (username) {
//   return username.length > 3;
// });

// console.log("filteredUserNames", filteredUserNames);

// var allProducts = [
//   { id: 1, name: "laptop", price: 170 },
//   { id: 2, name: "phone", price: 60 },
//   { id: 3, name: "tablet", price: 80 },
//   { id: 4, name: "water", price: 5 },
//   { id: 5, name: "soft drink", price: 10 },
// ];

// var filteredProducts = allProducts.filter(function (product) {
//   return product.price < 80;
// });
// console.log(filteredProducts);

// var sum = 0;
// allProducts.forEach(function (product) {
//   sum += product.price;
// });

// console.log("Total Price: ", sum);

// var scores = [19, 51, 90, 54, 100, 19];
// var number = 19;

// console.log(Array.isArray(scores));
// console.log(scores.lastIndexOf(19));
// console.log(scores.slice(2, 5));
// console.log(scores.join("-"));
// console.log(scores.reverse());

// var message = "hello-every-one";

// console.log(message.split("-"));

var word = prompt("Enter The word");
var characters = word.split("");
var reversed_chars = characters.reverse();
var newStr = reversed_chars.join("");
if (word == newStr) {
  console.log("Ok");
} else {
  console.log("Not Ok");
}
