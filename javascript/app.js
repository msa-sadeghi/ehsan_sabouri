let canvas = document.getElementById('canvas')
let ctx = canvas.getContext('2d')
let currentColor = 'black'
let isDrawing = false

canvas.addEventListener('mousedown', (e)=>{
    isDrawing = true
    ctx.beginPath()
    ctx.moveTo(e.offsetX, e.offsetY)
})

canvas.addEventListener('mousemove', (e)=>{
    if(isDrawing){
        ctx.lineTo(e.offsetX, e.offsetY)
        ctx.strokeStyle = currentColor
        ctx.stroke()
    }
})
canvas.addEventListener('mouseup', (e)=>{
    isDrawing = false
})


function changeColor(color){
    currentColor = color
}

function clearCanvas(){
    ctx.clearRect(0,0, canvas.width, canvas.height)
}