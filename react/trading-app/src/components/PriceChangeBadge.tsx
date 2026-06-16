
export default function PriceChangeBadge({priceChange}) {
  
  const isPositive = priceChange > 0
  const isNegative = priceChange < 0

  const color = isPositive ? "green" :
  isNegative ? "red" : "gray"

  const formatted = `${isPositive ? "+" : ""}${priceChange}`
  
  return (
    <span
    
    style={{color, fontWeight:"bold"}}
    >
      {formatted}
    </span>
  )
}
