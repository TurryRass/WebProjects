// What does document mean in JavaScript?
// A Document object represents the HTML document that is displayed in that window.
let sound = document.createElement('audio')
sound.setAttribute('src' , 'Resources/sound.mp3')
sound.loop = true;
sound.play()