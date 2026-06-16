import { useState } from "react";

function ProductCard({ product, handleDelete }) {
  const [isEditing, setIsEditing] = useState(false);
  const [formData, setFormData] = useState({ ...product });
  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]:
        e.target.name === "price"
          ? Number(e.target.value)
          : e.target.name === "in_stock"
            ? e.target.checked
            : e.target.value,
    });
  };
  const handleSave = () => {};
  return (
    <div>
      {isEditing ? (
        <div style={styles.card}>
          <label htmlFor="">name</label>
          <input
            onChange={handleChange}
            type="text"
            name="name"
            value={formData.name}
          />
          <br />
          <label htmlFor="">price</label>
          <input
            onChange={handleChange}
            type="number"
            name="price"
            value={formData.price}
          />
          <br />
          <label htmlFor="">in stock</label>
          <input
            onChange={handleChange}
            type="checkbox"
            name="in_stock"
            checked={formData.in_stock}
          />
          <br />
          <button onClick={handleSave}>Save</button>
          <button onClick={() => setIsEditing(false)}>Back</button>
        </div>
      ) : (
        <div style={styles.card}>
          <img style={styles.image} src={product.image} alt="" />
          <h3>{product.name}</h3>
          <p>{product.description}</p>
          <p>
            <strong>Price: {product.price}</strong>
          </p>
          <p>
            <strong>
              Status:
              {product.in_stock ? "In Stock" : "Out of stock"}
            </strong>
          </p>
          <button onClick={() => handleDelete(product.id)}>Delete</button>
          <button onClick={() => setIsEditing(true)}>Edit</button>
        </div>
      )}
    </div>
  );
}

export default ProductCard;

const styles = {
  card: {
    border: "1px solid #ddd",
    borderRadius: "10px",
    padding: "16px",
    width: "250px",
    boxShadow: "0 2px 8px rgba(0,0,0,0.1)",
  },
  image: {
    width: "100%",
    height: "150px",
    objectFit: "cover",
    borderRadius: "8px",
  },
  button: {},
};
