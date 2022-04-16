
// console.log(document.getElementById('ask-box').querySelectorAll('div'))
(document.getElementById('answer_nav').querySelectorAll('div').forEach(
    function(item){
        item.style.cursor = 'pointer'
        item.addEventListener('click',function(){
            alert(`please logout by clicking on ${item.innerText} on the coming page`)
            window.location.href = '/'
        })
    }
))
document.getElementById('ask-box').querySelectorAll('div').forEach(
    function(item,index){
        item.id = index + 5
        // item.style.border = ''
        item.addEventListener('click',function(){
            // alert(`item ${item} and ${index}`)
            // console.log(`item ${item} and ${index}`)
            // item.style.border = '2px solid green'
            window.location.href = `/ask/${item.id}`
        })
        // document.getElementById('confirm-class').addEventListener('click',function(){
        //     window.location.href = `/ask/${item.id}`
        // })
    }
)
