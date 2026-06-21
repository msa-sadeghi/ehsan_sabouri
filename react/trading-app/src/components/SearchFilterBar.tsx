
export default function SearchFilterBar() {
  return (
    <div>
        <input type="text"
        placeholder="search item ... "
        
        />
        <select name="" id="">
            <option value="">all</option>
            <option value="">Only Positive</option>
            <option value="">Only Negative</option>
        </select>

        <select name="" id="">
            <option value="">sort : name</option>
            <option value="">sort : price</option>
            <option value="">sort : price change</option>
        </select>

        <button></button>
    </div>
  )
}
