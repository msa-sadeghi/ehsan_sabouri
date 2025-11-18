let shoppinglist = []
let currentFilter = 'all'

function addItem(){
    const input = document.getElementById("itemInput")
    const itemName = input.value.trim()
    if(itemName === ''){
        alert("please enter product name")
        return
    }

    const newItem = {
        id: Date.now(),
        name : itemName,
        purchased:false
    }
    shoppinglist.push(newItem)
    input.value = ''
    input.focus()
    renderList()
    updateStats()

}

function renderList(){
    const listSection = document.getElementById('listSection')

    let filteredList = shoppinglist
    if(currentFilter === 'purchased'){
        filteredList = shoppinglist.filter(item => item.purchased)
    }else if(currentFilter === 'pending'){
        filteredList = shoppinglist.filter(item => !item.purchased)

    }
    if(filteredList.length === 0){
        listSection.innerHTML = `
        <div class="empty-state">
                <div style="font-size: 48px;">📝</div>
                <p>لیست خرید خالی است</p>
                <p style="font-size: 14px; margin-top: 10px;">موردی یافت نشد</p>
            </div>`
            return
    }
    const itemsHTML = filteredList.map((item, index) =>  `
    <div class="list-item">
        <div class="item-content">
            <div class="item-number">${index + 1}</div>
            <div class="item-name">${item.name}</div>
        </div>
    </div>
    `).join('')
    
    listSection.innerHTML = itemsHTML
}

function updateStats(){
    const total = shoppinglist.length
    const purchased = shoppinglist.filter(item => item.purchased).length
    const pending = total - purchased


    document.getElementById('totalItems').textContent = total
    document.getElementById('purchasedItems').textContent = purchased
    document.getElementById('pendingItems').textContent = pending
}