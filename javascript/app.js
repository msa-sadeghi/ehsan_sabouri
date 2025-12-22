let currentnumber = 10
let countdownElemet = document.getElementById('countdown')
let interval = null
function startCountdown(){
    currentnumber = 10
    countdownElemet.textContent = currentnumber
    interval = setInterval(()=>{
        currentnumber--
        countdownElemet.textContent = currentnumber
        if(currentnumber === 0){
            clearInterval(interval)
            setTimeout(()=>{
                countdownElemet.textContent = "s"
                setTimeout(()=>{
                    
                    countdownElemet.textContent = "10"
                }, 2000)
            }, 500)
        }
    }, 1000)
}

function stopCountdown(){
    if(interval !== null){
        clearInterval(interval)
        interval = null
        countdownElemet.textContent = "s"
                setTimeout(()=>{
                    
                    countdownElemet.textContent = "10"
                    currentnumber = 10
                }, 2000)

    }
}