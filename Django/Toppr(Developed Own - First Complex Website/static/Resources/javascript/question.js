
question_card = document.getElementsByClassName('question-card')

Object.values(question_card).forEach(function(element){
    // element.style.border = '2px solid black'
    element.querySelectorAll('div').forEach(function(el){
        if (el.classList.contains('choose')){
            el.addEventListener('click',function(){
                answer = document.getElementById(`answer_${element.id}`).innerText
                if(el.innerText.includes(answer)){
                    Object.values(element.getElementsByClassName('choose')).forEach(function(alu){
                        alu.style['pointer-events'] = 'none'
                    })
                    el.style.border = '1px solid green'
                    
                    // Object.values(document.getElementsByClassName('choose')).forEach(function(alu){
                    //     alu.style.border = '1px solid #e4e3e3'
                    // })
                }
                else{
                    Object.values(element.getElementsByClassName('choose')).forEach(function(alu){
                        alu.style['pointer-events'] = 'none'
                        if (alu.innerText.includes(answer)){
                            alu.style.border = '1px solid green'
                        }
                    })
                    el.style.border = '1px solid red'
                    
                    // Object.values(document.getElementsByClassName('choose')).forEach(function(alu){
                    //     alu.style.border = '1px solid #e4e3e3'
                    // })
                }
            })
        }
    })
})
