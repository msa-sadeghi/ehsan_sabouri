import { useState } from "react"

function ProductCard({productName, productCategory, price, inStock}){
    const [count, setCount] = useState(0)
    const incrementQuantity = () =>{
        setCount(count + 1)
    }
    return(
        <>
            <h3>{productName}</h3>
            <h4>{productCategory}</h4>
            <p>count: {count}</p>
            <p>price: {price.toLocaleString('fa-IR')}</p>
            <p style={{'color':inStock ? 'green' : 'red'}}>
                {inStock ?  'available' :  'notAvaialable'}</p>
            <button onClick={incrementQuantity}>increment</button>
        </>
    )
}

export default ProductCard