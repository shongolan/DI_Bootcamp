let listTasks = [];
let number=0
let w=document.getElementById("taskword")
let container=document.getElementById("listTasks")
function addTask(){
    if(w.value.length>0){
        listTasks.push(w.value)
        container.innerHTML+=`
        <div class="div" id="${w.value}">
             <button onclick="d(${number})"><i class="fas fa-times"></i></button>
             <input id="radio" type="radio" onclick="change(${number})">
             <p id="${w.value}">${w.value}</p>
        </div>`
        number++
        w.value=""
    }
    else{
        alert("please enter a tetxt")
    }    
}
function change(param){
    let r=document.getElementById(listTasks[param])
    r.style.textDecoration="line-through"
    r.style.color="red"
}
function d(index){
    document.getElementById(listTasks[index]).remove()
}
function c(){
    container.innerHTML=``
    listTasks=[]
}
