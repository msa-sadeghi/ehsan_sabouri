import { useState } from "react"
import { addProduct } from "../api/product"
function ProductForm(){
    const [formData, setFormData] = useState({
        name:"",
        description:"",
        price:"",
        in_stock:true
    })
    const handleSubmit = async (e)=>{
        e.preventDefault()
        try{

            await addProduct(formData)
        }
        catch(err){
            console.log(err)
        }
    }

    const handleChange = (e)=>{
        setFormData( {...formData, [e.target.name]:e.target.value}
        )
    }
    return(
        <form onSubmit={handleSubmit} style={styles.form}>
            <input type="text"
            name="name"
            value={formData.name}
            onChange={handleChange}
            placeholder="name.." />
            <input type="text"
            name="description"
            value={formData.description}
            onChange={handleChange}
            placeholder="description.." />
            <input 
            name="price"
            value={formData.price}
            onChange={handleChange}
            type="number" placeholder="price.." />
            <button>Add Product</button>
        </form>
    )
}

export default ProductForm

const styles = {
    form:{
        display:'flex', gap:'10px', margin:'10px 0'
    }
}