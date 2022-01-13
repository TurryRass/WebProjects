console.log('Welcome to Spotify!')

// See,that in js the variable in a function can be accessed in some other function too.

let gana_id = 1
let play_song_id = 0
let back = document.getElementById('back_btn')
let icon = document.getElementById('play_btn')
let next = document.getElementById('next_btn')
let song_title = document.getElementById('song_title')
let myProgressBar = document.getElementById('myProgressBar')
let m_ctrl_btn = Array.from(document.getElementsByClassName('m_ctrl_btn'))

m_ctrl_btn.forEach(function(element){
    element.addEventListener('click',()=>{
        play_song_id = parseInt(element.id)
        audioElement = document.getElementById(`im_song${play_song_id}`)
        song_title.innerText = document.getElementById(`song_title${play_song_id}`).innerText
        console.log(`gand_id${gana_id} and play_id${play_song_id}`)
        if(gana_id!=play_song_id){
            // alert('song schanged!')
            prev_song = document.getElementById(`im_song${gana_id}`)
            if(prev_song!=null){
                prev_song.pause()
                prev_song.currentTime = 0
                document.getElementById(`${gana_id}`).innerHTML = `
                <img src="/static/SiteResources/play-circle-regular.svg" alt="">
                `
            }
            else{
                gana_id = 1
            }
            console.log(gana_id)
            myProgressBar.value = 0
        }

        console.log('this is what',play_song_id)

        if(audioElement.paused || audioElement.currentTime <= 0){
            audioElement.play()
            document.querySelector('.bottom').style.display = 'flex'
            element.innerHTML = `<img src="/static/SiteResources/pause-circle-regular.svg" alt="">`
            icon.innerHTML = `            <img width='100%' height='110%' src="/static/SiteResources/pause-circle-regular.svg" alt="">`
            document.getElementById('gif').style.opacity = 1
        }
        else{
            // document.querySelector('.bottom').style.display = ''
            audioElement.pause()
            element.innerHTML = `
            <img src="/static/SiteResources/play-circle-regular.svg" alt="">
            `
            icon.innerHTML = `            <img width='100%' height='110%' src="/static/SiteResources/play-circle-regular.svg" alt="">`
            document.getElementById('gif').style.opacity = 0
        }
        
        audioElement.addEventListener('timeupdate',()=>{
            if(audioElement.currentTime == audioElement.duration){
                element.innerHTML = `<img src="/static/SiteResources/play-circle-regular.svg" alt="">`
                document.querySelector('.bottom').style.display = 'none'
            }
            // Update Seekbar When Song Starts
            progress = parseInt((audioElement.currentTime/audioElement.duration) * 100)
            myProgressBar.value = progress
        })
        
        // To make the song play that part where the seekbar has been rolled by the user
        myProgressBar.addEventListener('change',()=>{
            audioElement.currentTime = myProgressBar.value * audioElement.duration/100
        })
        gana_id = play_song_id
    })
})
icon.onclick = function (){
    if(audioElement.paused || audioElement.currentTime <= 0){
        audioElement.play()
        icon.innerHTML = `            <img width='100%' height='110%' src="/static/SiteResources/pause-circle-regular.svg" alt="">`
        document.getElementById(`${play_song_id}`).innerHTML = `
            <img src="/static/SiteResources/pause-circle-regular.svg" alt="">
        `
        // alert(document.getElementById(1).innerHTML)
        document.getElementById('gif').style.opacity = 1
    }
    else{
        audioElement.pause()
        icon.innerHTML = `            <img width='100%' height='110%' src="/static/SiteResources/play-circle-regular.svg" alt="">`
        document.getElementById(`${play_song_id}`).innerHTML = `
            <img src="/static/SiteResources/play-circle-regular.svg" alt="">
        `
        document.getElementById('gif').style.opacity = 0
    }
}

back.onclick = function(){
    audioElement.pause()
    audioElement = document.getElementById(`im_song${play_song_id-1}`)
    document.getElementById(`${play_song_id-1}`).click()
}

next.onclick = function(){
    audioElement.pause()
    audioElement = document.getElementById(`im_song${play_song_id+1}`)
    document.getElementById(`${play_song_id+1}`).click()
}