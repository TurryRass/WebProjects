setInterval(() => {
    let date = new Date
    htime = date.getHours()
    mtime = date.getMinutes()
    stime = date.getSeconds()

    hrotations = 30*htime
    mrotations = 6*mtime
    srotations = 6*stime

    hour.style.transform = `rotate(${hrotations}deg)`
    minute.style.transform = `rotate(${mrotations}deg)`
    second.style.transform = `rotate(${srotations}deg)`

}, 1000);