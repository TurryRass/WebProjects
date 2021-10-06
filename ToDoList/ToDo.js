function DisplayToDo() {
    if (localStorage.getItem('ToDoJson') != null) {
        let ToDoStr = localStorage.getItem('ToDoJson');
        let ToDoJsonArray = JSON.parse(ToDoStr)
        let TableBody = document.getElementById('Table')
        let str = ""
        ToDoJsonArray.forEach((element, index) => {
            str += `
        <tr>
        <td>${index + 1}</td>
        <td>${element[0]}</td>
        <td><Button class='delete' onclick='Deleted(${index})'>Delete</Button>
            <Button class='view'>Desc</Button>
        </td>
        </tr>
    `
        });
        TableBody.innerHTML = str;
    }
    else {
        alert(
            'Welcome User!Thank You For Visiting Our Website!'
        )
    }
}
document.onload = DisplayToDo()
document.getElementById("submit").onclick = () => {
    // localStorage.setItem()
    console.log("hello!");
    title = document.getElementById("head").value;
    desc = document.getElementById("desc").value;
    if (localStorage.getItem("ToDoJson") == null) {
        ToDoJsonArray = [];
        if (title == '') {
            title = 'None'
        }
        ToDoJsonArray.push([title, desc]);
        localStorage.setItem("ToDoJson", JSON.stringify(ToDoJsonArray))
    }

    else {
        ToDoStr = localStorage.getItem("ToDoJson")
        ToDoJsonArray = JSON.parse(ToDoStr)
        if (ToDoJsonArray.length == 10) {
            alert('No more ToDo can be added!');
        }
        else {
            if (title == '') {
                title = 'None'
            }
            ToDoJsonArray.push([title, desc]);
            localStorage.setItem("ToDoJson", JSON.stringify(ToDoJsonArray))
        }
    }
    let TableBody = document.getElementById('Table')
    let str = ""
    ToDoJsonArray.forEach((element, index) => {
        str += `
        <tr>
        <td>${index + 1}</td>
        <td>${element[0]}</td>
        <td><Button class='delete' onclick='Deleted(${index})'>Delete</Button>
            <Button class='view'>Desc</Button>
        </td>
        </tr>
    `
    });
    TableBody.innerHTML = str;

}

function Deleted(item) {
    console.log(item, 'Deleted!')
    ToDoStr = localStorage.getItem('ToDoJson');
    ToDoJsonArray = JSON.parse(ToDoStr);
    console.log(ToDoJsonArray)
    ToDoJsonArray.splice(item, 1);
    // localStorage.clear()
    localStorage.setItem('ToDoJson', JSON.stringify(ToDoJsonArray))
    DisplayToDo()
}

function allDelete(){
    console.log('great!')
    localStorage.clear();
    location.reload()
}


