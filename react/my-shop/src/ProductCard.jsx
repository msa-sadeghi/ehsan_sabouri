import { useState } from "react"

function ProductCard({product}){
    const [quantity, setQuantity] = useState(1)
    const [selectedColor, setSelectedColor] = useState(product.colors[0])
    const [inCart, setInCart]= useState(false)    
    const totalPrice = product.price * quantity
    const  handleAddToCard = ()=>{
        if(product.inStock){
            setInCart(true)
            alert(`${quantity} number ${product.name} added to card`)
        }
    }
    return(
        <div className="product-card">
          
            <div className="product-image">
                <img src={product.image} alt={product.name} />
                {!product.inStock && <div>not found</div>}
            </div>
            <h3>{product.name}</h3>
            <p className="price">
                {
                    product.inStock ?  
                    product.price.toLocaleString('fa-IR')+'تومان':
                    'ناموجود'
                }
            </p>
            <div className="color-selector">
                <label htmlFor="">color:</label>
                <select name="" id=""
                
                 value={selectedColor}
                 onChange={(e)=>setSelectedColor(e.target.value)}
                 disabled={!product.inStock}
                >
                    {product.colors.map((c)=>(
                        <option key={c} value={c}>{c}</option>
                    ))}
                </select>
            </div>
            <div className="quantity-selector">
                <label htmlFor="">count:</label>
                <button
                disabled={!product.inStock}
                onClick={()=>setQuantity(Math.max(1,quantity-1))}
                >-</button>
                <button
                disabled={!product.inStock}
                onClick={()=>{
                    setQuantity(quantity => quantity+1)

                }}
                >+</button>
                <span>{quantity.toLocaleString('fa-IR')}</span>
            </div>
            <div className="total">
                total:{totalPrice.toLocaleString('fa-IR')}تومان
            </div>
            {product.inStock ? (
                <button
                onClick={handleAddToCard}
                disabled={inCart}
                >
                    {inCart ? 'is in cart' : 'add to cart'}
                    
                </button>
            ) : (
                <button>Inform me when is available</button>
            )}
        </div>
    )
}

export default ProductCard