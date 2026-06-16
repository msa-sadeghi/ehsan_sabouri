import { useEffect, useState } from "react"
import "./assets/css/styles.css"
import Loading from "./components/Loading"
import MarketOverview from "./components/MarketOverview"
function App() {
  const [items, setItems] = useState([])
  const [loading, setLoading] = useState(true)
  const [currentPage, setCurrentPage] = useState(1)
  const itemsPerPage = 20
  useEffect(()=>{
    async function getData() {
      const response = await fetch("https://brsapi.ir/Api/Tsetmc/Sample/Api_FreeBourseWebService.json")
      const data = await response.json()
      console.log(data[0])
      setItems(data)
      setLoading(false)
    }
    
    const intervalID = setInterval(getData, 5000)
    return ()=>clearInterval(intervalID)
  }, [])

    const totalPages = Math.ceil(items.length / itemsPerPage)
    const startIndex = (currentPage - 1) * itemsPerPage
    const currentItems =  items.slice(
      startIndex, startIndex + itemsPerPage
    )
    console.log(currentItems)
  return (
    <>
     <h1>Trading App</h1>
     {loading && <Loading/>}
     
     <div className="card-container">
      {currentItems.map(it => (
      <MarketOverview key={it.id} item = {it} />
     ))}
     </div>
     <button 
     onClick={()=> setCurrentPage(currentPage - 1)}
     disabled={currentPage === 1}>Prev</button>
     <button 
     onClick={()=> setCurrentPage(currentPage + 1)}
     disabled={currentPage === totalPages}>Next</button>
    </>
  )
}

export default App
