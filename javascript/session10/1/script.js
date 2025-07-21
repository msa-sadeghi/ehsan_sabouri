let audioElement = document.querySelector('audio')
let timeElement = document.querySelector("#time")

function playHandler(){
    audioElement.play()
    setInterval(function(){
        timeElement.innerHTML = '00:' + '0' + Math.floor(audioElement.currentTime)
    }, 1000)
}
function pauseHandler(){
    audioElement.pause()
}
function durationHandler(){
    console.log(audioElement.duration)
}
function currentTimeHandler(){}
function playBackRateHandler(){
    audioElement.playbackRate = 2
}