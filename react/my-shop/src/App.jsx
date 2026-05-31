import './App.css'
import ProductsPage from './components/ProductsPage'
import ProductForm from './components/ProductForm'

function App() {
  return (
    <div className="container">
      <h1>Online Shop</h1>
      <ProductForm/>
      <ProductsPage/>
    </div>
    
  )
}

export default App
