const image = document.querySelector("#cover")
const title = document.querySelector("#title")
const artist = document.querySelector("#artist")
const music = document.querySelector("audio")
const currentTime = document.querySelector("#current-time")
const duration = document.querySelector("#duration")
const progress = document.querySelector("#progress")
const progressContainer = document.querySelector("#progress-container")
const prev = document.querySelector("#prev")
const play = document.querySelector("#play")
const next = document.querySelector("#next")
const background = document.querySelector("#background")
const songs = [
    {
        path:"./media/bazar.m4a",
        displayName: "Html Padcast",
        artist: "jack",
        cover:"https://images.genius.com/ee202c6f724ffd4cf61bd01a205eeb47.1000x1000x1.jpg"

    },
    {
        path:"./media/html.m4a",
        displayName: "blala Padcast",
        artist: "niki",
        cover:"https://images.genius.com/c5a58cdaab9f3199214f0e3c26abbd0e.1000x1000x1.jpg"

    },
]