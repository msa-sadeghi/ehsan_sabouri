function Pagination({page}){
    return(
        <div>
            <button>Previous</button>
            <button>Page: {page}</button>
            <button>Next</button>
        </div>
    )
}

export default Pagination