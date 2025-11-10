let calculateHistory = []
function add(a,b){
    return a + b
}
function subtract(a,b){
    return a - b
}
function multiply(a,b){
    return a * b
}
function divide(a,b){
    if(b === 0){
        return "error zero division"
    }
    return a / b
}

const factorial = (n) => {
    if(n < 0) return " number is negative"
    if (n === 0 || n === 1) return 1
    let result = 1
    for(let i = 2; i<=n; i++)
        result *= i
    return result
}

function power(base , exponent){
    return Math.pow(base, exponent)
}
function modulus(a , b){
    return a % b
}
const sqrt = num => Math.sqrt(num)
const square = num => num * num

function calculateBasic(){
    let basicNum1 = document.getElementById("basicNum1").value
    let basicNum2 = document.getElementById("basicNum2").value
    let op = document.getElementById("basicOp").value
    let basicResult = document.getElementById("basicResult")
    let result = 0
    let opSymbol
    if(op === "add"){
        result = add(Number(basicNum1), Number(basicNum2))
        opSymbol = "+"
    }

    basicResult.innerHTML = result
    basicResult.classList.add("show")
    addToHistory(`عملیات پایه : ${basicNum1} ${opSymbol} ${basicNum2} = ${result}`)
}

function addToHistory(calculation){
    calculateHistory.unshift(calculation)
    if(calculateHistory.length > 10){
        calculateHistory.pop()
    }
    updateHistoryDisplay()
}

function updateHistoryDisplay(){
    const historyList =  document.getElementById("historyList")
    if(calculateHistory.length === 0){
        historyList.innerHTML = '<p>هیچ تاریخچه ای وجود ندارد</p>'
        return
    }
    historyList.innerHTML = calculateHistory.map(item => `<div>${item}</div>`).join('')
    console.log(typeof historyList.innerHTML)
}

function clearHistory(){
    calculateHistory = []

    updateHistoryDisplay()

}