import { fetchProducts, deleteProduct } from "../api/product"
import { useState } from "react"
import ProductCard from "./ProductCard"
import Pagination from "./Pagination"
function ProductsPage(){
    const [products, setProducts] = useState([])
    const [page, setPage] = useState(1)
    const [perPage, setPerPage] =  useState(1)
    const [totalPages, setTotalPages] = useState(1)
    async function loadProducts(currentPage) {
        const data = await fetchProducts(currentPage, perPage)
        setProducts(data.items)
        setPage(data.page)
        setTotalPages(data.totalPages)
        
    }
    loadProducts(page)
    function handlePrev(){
        if (page > 1) setPage((prev) => prev - 1)
        }
    function handleNext(){
        if (page < totalPages) setPage((prev) => prev + 1)

    }
    return(
        <div>
            {products.map((product) => (
                <ProductCard key={product.id} product={product}/>
            ))}
            <Pagination
            page={page}
            />
        </div>
    )
}

export default ProductsPage