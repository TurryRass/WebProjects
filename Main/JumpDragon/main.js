// function sound(){
//     let bgMusic = document.createElement('audio')
//     bgMusic.setAttribute('src','Resources/music.mp3')
//     bgMusic.loop = true
//     bgMusic.play()
// }

// function cheekh(){
//     let cheekh = document.createElement('audio')
//     cheekh.setAttribute('src','Resources/gameover.mp3')
//     cheekh.play()
// }

animspeed = 0

var sound = new Audio('Resources/music.mp3')
var cheekh = new Audio('Resources/gameover.mp3')
sound.play()

var score = 0
var cross = true
document.onkeydown = function jumper(e) {
    // console.log(e.keyCode)
    if (e.keyCode == 87) {
        // console.log('w has been pressed.')
        dino = document.querySelector('.dino');
        dino.classList.add('animateDino')
        setTimeout(() => {
            dino.classList.remove('animateDino')
        }, 700);
    }
    if (e.keyCode == 68) {
        let dino = document.querySelector('.dino');
        left = parseInt(window.getComputedStyle(dino,null).getPropertyValue('left'))
        dino.style.left = left + 240 + 'px'
        dino.style.transform = `scaleX(${1})`
    }
    if (e.keyCode == 65) {
        let dino = document.querySelector('.dino');
        left = parseInt(window.getComputedStyle(dino,null).getPropertyValue('left'))
        dino.style.left = left - 240 + 'px';
        dino.style.transform = `scaleX(${-1})`
    }
}

grat = setInterval(() => {
    let dino = document.querySelector('.dino')
    let dragon = document.querySelector('.dragon')
    let gameOver = document.querySelector('.Screen')
    let speeddragon = document.querySelector('.dragonMove')

    dx = (parseInt(window.getComputedStyle(dino, null).getPropertyValue('left')))
    dy = (parseInt(window.getComputedStyle(dino, null).getPropertyValue('top')))
    ox = (parseInt(window.getComputedStyle(dragon, null).getPropertyValue('left')))
    oy = (parseInt(window.getComputedStyle(dragon, null).getPropertyValue('top')))
    animdur = (parseFloat(window.getComputedStyle(speeddragon, null).getPropertyValue('animation-duration')))

    offsetX = Math.abs(dx - ox)
    offsetY = Math.abs(oy - dy)

    if (offsetX <= 180 && offsetY < 52){
        sound.pause()
        setTimeout(() => {
            cheekh.play()
        }, 500);
        gameOver.innerHTML = '<b>GameOver</b>'
        dragon.style.left = 105 + 'vw';
        dragon.classList.remove('dragonMove')
        dino.style.left = 50 + 'px'
        setTimeout(() => {
            alert('Game is Over.Click OK to play again!')
            location.reload()
        }, 500);
    }
    else if(offsetX <= 230 && offsetY >= 100 && cross == true){
        score += 100
        Score = document.querySelector('#Score')
        Score.innerHTML =  'Score:' + String(score)
        cross = false
        setTimeout(() => {
            animspeed += 0.2
            if (animspeed >= 1.8){
                animspeed = 1.8
            }
            animdur = 5
            console.log(animspeed)
            console.log(animdur)
            console.log(dragon.style.animationDuration = (animdur - animspeed) + 's')
        }, 500);
        setTimeout(() => {
            cross = true
        }, 500);
    }
}, 150);