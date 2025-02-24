var allProducts = [
    { id: 1, name: "laptop", price: 17000000 },
    { id: 2, name: "phone", price: 7000000 },
    { id: 3, name: "milk", price: 35000 },
    { id: 4, name: "pen", price: 12000 },
    { id: 5, name: "pencil", price: 9000 },
    { id: 6, name: "cable", price: 55000 },
    { id: 7, name: "water", price: 6000 },
    { id: 8, name: "soft drink", price: 13000 },
  ];

  var userBasket = [
    {id:1, name:"milk", price:35000},
    {id:2, name:"water", price:6000}
  ]

  var userRequest = prompt("1.Add product \n 2.Remove Product");
  if (userRequest === "1"){
    var userProductName = prompt("Enter product name");
    var productData;
    var isInShop = allProducts.some(function(p){
        if(p.name === userProductName){
            productData = p;
            return true;
        }
    });
    if(isInShop === true){
        var newProduct = {
            id:3,
            name:productData.name,
            price:productData.price,
        };
        userBasket.push(newProduct);
        console.log("Basket", userBasket)
    }

  } else if (userRequest === "2"){
    var userProductName = prompt("Enter your product name")
    var userProductIndex = userBasket.findIndex(function(p){
        return p.name === userProductName
    });
    userBasket.splice(userProductIndex, 1);
    console.log("Basket", userBasket)
  }

  var users = ['Ali', 'Amin', 'Amir', 'Babak', 'Hasan']