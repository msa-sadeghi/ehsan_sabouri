products =  []

function addProduct(){
    let productName = document.getElementById("productName").value;
    let productCategory = document.getElementById("productCategory").value;
    let productPrice = document.getElementById("productPrice").value;
    let productStock = document.getElementById("productStock").value;
    let productDesc = document.getElementById("productDesc").value;

    let p = new Product(productName,
         productCategory, productPrice, 
         productStock, productDesc)
                    products.push(p)
    renderProducts()
    saveToStorage()
}

function loadFromStorage(){
    let stored = localStorage.getItem('products')
    let parsed = JSON.parse(stored)
    products = parsed.map(p=>{
        let product = new Product
    })
}

function saveToStorage(){
    localStorage.setItem('products', JSON.stringify(products))
}


function Product(name, category, price, stock, description){
    this.id = Date.now()
    this.name = name
    this.category = category
    this.price = price
    this.stock = stock
    this.description = description
}

function renderProducts(){
    let grid =  document.getElementById("productsGrid")
    if(products.length === 0){
        grid.innerHTML = `
            <div>
                <div>
                    <p>
                        محصولی یافت نشد
                    </p>
                </div>
            </div>
        `
        return
    }
    grid.innerHTML =  products.map(p => `
            <div class="product-card">
                <div class="product-name">${p.name}</div>
                <div class="product-category">${p.category}</div>
                <div class="product-price">${p.price}</div>
                <div class="product-stock">${p.stock}</div>
                <div >${p.description}</div>
                <div class="product-actions">
                <button class="btn-success">
                افزایش
                </button>

                <button class="btn-danger">
                حذف
                </button>
                </div>
        `)
}

loadFromStorage()
renderProducts()