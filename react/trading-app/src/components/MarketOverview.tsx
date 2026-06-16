import PriceChangeBadge from "./PriceChangeBadge"
export default function MarketOverview({item}) {
    const  {pc, py, l18, pcp} = item
    
  return (
    <div className="card">
      <PriceChangeBadge priceChange={pcp}/>
      <p>name :  {l18}</p>
        <p>today's price  : {pc}</p>
        <p>yesterday's price  : {py}</p>
    </div>
  )
}
