let  products = [
    {name: "shoe", price:85, inStock:true},
    {name: "bag", price:96, inStock:false},
    {name: "watch", price:60, inStock:true},
]

let availabeWithDiscount = products
.filter(pr => pr.inStock)
.map(pr => ({
    name : pr.name,
    originalPrice: pr.price,
    discountedPrice :  pr.price * 0.9 
}))

console.log(availabeWithDiscount)