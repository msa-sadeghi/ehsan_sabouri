function ProductCard({product}){
    return(
        <div style={styles.card}>
            <img style={styles.image} src={product.image} alt="" />
            <h3>{product.name}</h3>
            <p>{product.description}</p>
            <p><strong>Price: {product.price}</strong></p>
            <p><strong>Status:
                {product.in_stock ? 'In Stock' : "Out of stock"}
                </strong></p>
            <button>Delete</button>
        </div>
    )
}

export default ProductCard

const styles = {
    card:{
        border:"1px solid #ddd",
        borderRadius : "10px",
        padding:"16px",
        width:"250px",
        boxShadow:"0 2px 8px rgba(0,0,0,0.1)"
    },
    image:{
        width:"100%",
        height:"150px",
        objectFit:"cover",
        borderRadius:'8px'
    },
    button:{

    }
}