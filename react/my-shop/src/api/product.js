const BASE_URL = 'http://127.0.0.1:5000'

export async function fetchProducts(page = 1, perPage = 10) {
    const response = await fetch(`${BASE_URL}/products?page=${page}&per_page=${perPage}`)
    if(!response.ok){
        throw new Error("Failed to fetch products")
    }
    return await response.json()
}

export async function deleteProduct(id) {
    const response = await fetch(`${BASE_URL}/products/${id}`,{method: "DELETE"})
    if(!response.ok){
        throw new Error("Failed to delete product")
    }
    return await response.json()
}
