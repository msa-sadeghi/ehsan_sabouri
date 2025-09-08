// console.log(a)
// var a = 10;



// foo();
// function foo(){console.log("hello")}


// function a(){
//     console.log("a")
//     b()
// }

// function b(){
//     console.log("b")
//     c()
// }

// function c(){
//     console.log("c")
// }
// a()


// function my(){
//     let x = 10
// }
// my()
// console.log(x)

// {
//     var x = 12
// }

// console.log(x)

// function outer(){
    
//     function inner(){
//         let x = 10
//     }
//     console.log(x)
//     return inner
// }

// let fn = outer()
// fn()

// function counter(){
//     let count = 0
//     return function(){
//         count++
//         return count
//     }
// }

// const c1 = counter()
// console.log(c1())
// console.log(c1())
// const c2 = counter()
// console.log(c2())

// let data = []

// setInterval(function(){
//     new Array().fill("")
//     data = null
// }, 1000)

// let obj = {}
// obj = null

// let user = {}

// Object.defineProperty(user, "id", {
//     value:1,
//     writable:false,
//     enumerable:false,
//     configurable:false
// })

// console.log(user.id)
// user.id = 345
// console.log(user.id)


let animal = {
    eats:true
}

// let dog = {
//     barks:true
// }
// console.log(dog.eats)
// dog.__proto__ = animal
// console.log(dog.eats)

// let cat = Object.create(animal)
// cat.meow = true
// console.log(cat.eats)
// console.log(cat.meow)

// function Person(name){
//     this.name = name
// }
// Person.prototype.sayHi = function(){
//     console.log(`${this.name} is saying Hi`)
// }
// let sara = new Person("sara")
// console.log(sara.name)
// sara.sayHi()
// let reza = new Person("reza")
// console.log(reza.name)
// reza.sayHi()


// let id = Symbol("id")

// let user = {
//     name:"sara",
//     [id]:1,
//     [id]:2
// }
// let user2 = {
//     name:"reza",
//     [id]:1
// }
// console.log(user[id])
// console.log(user2[id])



// let arr = [1,2,3,4]

// let it = arr[Symbol.iterator]()
// console.log(it.next())
// console.log(it.next())


// function* gen(){
//     yield 1
//     yield 2
//     yield 3
// }

// let g = gen()
// console.log(g.next())
// console.log(g.next())

function my(another){
    console.log("blalala")
    another()
}

function another(){
    console.log("another")
}

my(another)