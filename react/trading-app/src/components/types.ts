export interface MarketItem{
    l18:string
    pc:number
    py:number
    pcp:number

}

export type FilterType = "all" | "positive" | "negative"
export type SortField =  "name" | "price" | "change"
export type SortDirection = "asc" | "desc"