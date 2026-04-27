import ProductCard from "./ProductCard"
import { useEffect, useState } from "react"
function ProductList(){
  const [products, setProducts] =  useState([])
  useEffect(()=>{
        fetch('http://127.0.0.1:5000/all')
        .then(res=>res.json())
        .then(data=>setProducts(data))
    }, [])

  return(
    <div className="product-grid">
        {products.map((p)=>(
            <ProductCard key={p.id} product={p}/>
        ))}
    </div>
  )
}
export default ProductList