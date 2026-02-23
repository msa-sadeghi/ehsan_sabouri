import './App.css'
import ProductCard from './ProductCard'


function App() {

  return (
    <>
    <ProductCard 
    productName="laptop" 
    productCategory="electronic"
    inStock={false}
    price = {10000000}
    />
    <ProductCard 
    productName="laptop2" 
    productCategory="electronic"
    inStock={true}
    price = {10000000}
    />
    
    </>
    
  )
}

export default App
