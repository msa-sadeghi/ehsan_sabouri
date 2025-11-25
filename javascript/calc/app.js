// let shoppinglist = []
// let currentFilter = 'all'

// function addItem(){
//     const input = document.getElementById("itemInput")
//     const itemName = input.value.trim()
//     if(itemName === ''){
//         alert("please enter product name")
//         return
//     }

//     const newItem = {
//         id: Date.now(),
//         name : itemName,
//         purchased:false
//     }
//     shoppinglist.push(newItem)
//     input.value = ''
//     input.focus()
//     renderList()
//     updateStats()

// }

// function renderList(){
//     const listSection = document.getElementById('listSection')

//     let filteredList = shoppinglist
//     if(currentFilter === 'purchased'){
//         filteredList = shoppinglist.filter(item => item.purchased)
//     }else if(currentFilter === 'pending'){
//         filteredList = shoppinglist.filter(item => !item.purchased)

//     }
//     if(filteredList.length === 0){
//         listSection.innerHTML = `
//         <div class="empty-state">
//                 <div style="font-size: 48px;">📝</div>
//                 <p>لیست خرید خالی است</p>
//                 <p style="font-size: 14px; margin-top: 10px;">موردی یافت نشد</p>
//             </div>`
//             return
//     }
//     const itemsHTML = filteredList.map((item, index) =>  `
//     <div class="list-item">
//         <div class="item-content">
//             <div class="item-number">${index + 1}</div>
//             <div class="item-name">${item.name}</div>
//         </div>
//         <div class-"item-actions">
//             <button class="btn ${item.purchased ? 'btn-success' : 'btn-warning'}
//             btn-small" onclick="togglePurchased(${item.id})">
//                 ${item.purchased ? 'بازگشت' : 'خریداری شد'}
//             </button>
//         </div>
//     </div>
//     `).join('')
    
//     listSection.innerHTML = itemsHTML
// }

// function togglePurchased(id){
//     shoppinglist.forEach(item => {
//         if(item.id === id){
//             item.purchased = !item.purchased
//         }
//     })
//     renderList()
//     updateStats()
// }


// function updateStats(){
//     const total = shoppinglist.length
//     const purchased = shoppinglist.filter(item => item.purchased).length
//     const pending = total - purchased


//     document.getElementById('totalItems').textContent = total
//     document.getElementById('purchasedItems').textContent = purchased
//     document.getElementById('pendingItems').textContent = pending
// }

// function clearPurchased(){
//     const purchasedCount = shoppinglist.filter(item => item.purchased).length
//     if(purchasedCount === 0){
//         alert("nothin found")
//         return
//     }
//     if(confirm(`Are you sure to delete ${purchasedCount} items?`)){
//         shoppinglist = shoppinglist.filter(item => !item.purchased)
//         renderList()
//         updateStats()
//     }
// }

// let numbers = [10, 12, 13, 14, 15]
// let sum = numbers.reduce((accumulator, current, currentIndex, another) =>{
//     console.log(`accumulator: ${accumulator}`)
//     console.log(`current: ${current}`)
//     console.log(`currentIndex: ${currentIndex}`)
//     console.log(`array: ${another}`)
   

//     return accumulator + current
// })
// console.log(sum)

// let cart = [
//     {name: "shoe", price:1000, quantity:1},
//     {name: "bag", price:4000, quantity:2},
//     {name: "another", price:500, quantity:4},
// ]

// let totalPrice = cart.reduce((total, item)=>{
 
//     return total + item.quantity * item.price
// }, 0)

// console.log(totalPrice)

let keys = ["name",  "age", "city"]
let values = ["sara", 32, "teh"]

let obj = keys.reduce((object, key, index)=>{
    object[key] = values[index]
    return object
}
, {})

console.log(obj)

let users = [
    {id:1, name:"sara"},
    {id:2, name:"artin"},
    {id:3, name:"arman"}
]

let t = users.reduce((obj, user)=>{
    obj[user.id] = user.name
    return obj
},
 {})
 console.log(t)