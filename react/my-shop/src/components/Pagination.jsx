function Pagination({page, handlePrev, handleNext}){
    return(
        <div>
            <button onClick={handlePrev}>Previous</button>
            <button>Page: {page}</button>
            <button onClick={handleNext}>Next</button>
        </div>
    )
}

export default Pagination