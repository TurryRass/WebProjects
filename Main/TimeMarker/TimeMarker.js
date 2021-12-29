const options = { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric', }
setInterval(() => {

    let time = new Date();
    if (time.getHours().length == 1) {
        time.getHours() = '0' + 0
    }
    if (time.getMinutes().length == 1) {
        time.getMinutes() = '0' + 0
    }
    if (time.getSeconds().length == 1) {
        time.getSeconds() = '0' + 0
    }
    let date = time.toLocaleDateString(undefined, options);
    let Time = time.getHours() + ':' + time.getMinutes() + ':' + time.getSeconds();
    document.getElementById('time').innerHTML = Time + "<br>on " + date;

}, 1000);