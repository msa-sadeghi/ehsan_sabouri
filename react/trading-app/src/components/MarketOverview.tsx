import PriceChangeBadge from "./PriceChangeBadge"
import type { MarketItem } from "./types"
export default function MarketOverview({item}: MarketItem) {
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
