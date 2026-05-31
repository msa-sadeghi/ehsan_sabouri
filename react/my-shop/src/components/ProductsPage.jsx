import { fetchProducts, deleteProduct } from "../api/product"
import { useEffect, useState } from "react"
import ProductCard from "./ProductCard"
import Pagination from "./Pagination"
import Loading from "./Loading"

function ProductsPage(){
    const [products, setProducts] = useState([])
    const [page, setPage] = useState(1)
    const [perPage, setPerPage] =  useState(1)
    const [totalPages, setTotalPages] = useState(1)
    const [loading, setLoading] = useState(false)
    async function loadProducts(currentPage) {
        try{

            setLoading(true)
            const data = await fetchProducts(currentPage, perPage)
            setProducts(data.items)
            setPage(data.page)
            setTotalPages(data.total_pages)
        }catch(err){
            console.log("error")
        }finally{

            setLoading(false)
        }
        
    }
    useEffect(()=>{
        loadProducts(page)
    }, [page])
    function handlePrev(){
        if (page > 1) setPage((prev) => prev - 1)
        }
    function handleNext(){
        if (page < totalPages) setPage((prev) => prev + 1)

    }
     async function handleDelete(id) {
        try{
            await deleteProduct(id)
            await loadProducts(page)

        }catch(err){
            console.log("error")
        }
    }
    return(
        <div>
            {loading && <Loading/>}
            {products.map((product) => (
                <ProductCard key={product.id} product={product} handleDelete={handleDelete}/>
            ))}
            <Pagination
            page={page}
            handlePrev={handlePrev}
            handleNext={handleNext}
            />
        </div>
    )
}

export default ProductsPage