var name= prompt("What is your Name?", "");
var result= document.getElementById("new");
if(name=="" || name==false ){
   
   result.innerHTML="Name not set";
}else{
    var values={};
   var ts=document.getElementById("table");
   var tr=document.createElement("tr");
   var td=document.createElement("td");
   var tbody=document.createElement("tbody");
    console.log(ts);
   var txt=document.createTextNode(name);
   td.appendChild(txt);
   tr.appendChild(td);
   tbody.appendChild(tr);
   ts.appendChild(tbody);
  
}
function add_user(){
  alert(name); 


}
function delete_task(el){
    quest=confirm("Do you want to delete it")
    if(quest){
        el.remove();
        result.innerHTML="Task deleted Successfully";
      
    }else{
        alert("ok");
        result.innerHTML="You deleted Nothing";
    }
}

document.getElementById("first").innerHTML="Hello world";


