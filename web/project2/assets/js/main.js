function clickOnBars(){
    var nav_elem = document.getElementById("menu");
    if (nav_elem.className === ""){
        nav_elem.className += "responsive";
    }
    else{
        nav_elem.className = ""
    }
}