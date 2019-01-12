//
// functions to check if forms have valid data
//
function checkAddToolForm(e) {
    let name = $("#inputNewToolName").val();
    console.log(name)
    if (!$("#inputNewToolName").val()){
        $("#inputNewToolName").addClass('is-invalid');
    } else {
        $("#inputNewToolName").removeClass('is-invalid');
    }
    let desc = $("#inputNewToolDesc").val();
    console.log(desc)
    if (!$("#inputNewToolDesc").val()) {
        $("#inputNewToolDesc").addClass('is-invalid');
    } else {
        $("#inputNewToolDesc").removeClass('is-invalid');
    }
    let price = $("#inputPrice").val();
    console.log(price)
    if (!$("#inputPrice").val()) {
        $("#inputPrice").addClass('is-invalid');
    } else {
        $("#inputPrice").removeClass('is-invalid');
    }
    let file = $("#inputFile").val();
    console.log(file)
    if (!$("#inputFile").val()) {
        $("#inputFile").addClass('is-invalid');
    } else {
        $("#inputFile").removeClass('is-invalid');
    }
    let date = $("#inputDate").val();
    console.log(date)
    if (!$("#inputDate").val()) {
        $("#inputDate").addClass('is-invalid');
    } else {
        $("#inputDate").removeClass('is-invalid');
    }
    if (!name || !desc || !price || !file || !date) {
        e.preventDefault();
        alert("Not every field has beed filled!");
    } 
}
function checkUserPanelForm(e) {
    console.log("in")
    let email = $("#inputEmail");   
    let emailRes = false;
    if (!email.val() || email.val() == "None"){
        email.addClass('is-invalid');
    } else {
        email.removeClass('is-invalid');
        emailRes = true;
    }
    let name = $("#inputName");   
    let nameRes=false;
    if (!name.val() || name.val() == "None") {
        name.addClass('is-invalid');
    } else {
        name.removeClass('is-invalid');
        nameRes = true;
    }
    let surname = $("#inputSurname");  
    let surnameRes = false;  
    if (!surname.val() || surname.val() == "None") {
        surname.addClass('is-invalid');
    } else {
        surname.removeClass('is-invalid');
        surnameRes = true;
    }
    let adress = $("#inputAdress");    
    let adressRes = false;
    if (!adress.val() || adress.val() == "None") {
        adress.addClass('is-invalid');
    } else {
        adress.removeClass('is-invalid');
        adressRes = true;
    }    
    if (!emailRes || !nameRes || !surnameRes || !adressRes) {
        e.preventDefault();
        alert("'None' is not a correct value. Please fill all inputs with correct values!");
    } 
}
function returnToolFormCheck(e) {
    console.log("in")
    let file = $("#inputFile");   
    let fileRes = false;
    if (!file.val()){
        file.addClass('is-invalid');
    } else {
        file.removeClass('is-invalid');
        fileRes = true;
    }
    let condition = $("#inputCondition");   
    let conditionRes=false;
    if (!condition.val()) {
        condition.addClass('is-invalid');
    } else {
        condition.removeClass('is-invalid');
        conditionRes = true;
    }    
    if (!fileRes || !conditionRes) {
        e.preventDefault();
        alert("Please fill all inputs!");
    } 
}
function bookToolFormCheck(e) {
    console.log("in")
    let date = $("#inputDate"); 
    let dateVal = new Date(date.val())
    let dateToday = new Date()
    let dateRes = false;
    if (dateVal.getDate() < dateToday.getDate()){
        date.addClass('is-invalid');
    } else {
        date.removeClass('is-invalid');
        dateRes = true;
    }
    
    if (!dateRes) {
        e.preventDefault();
        alert("You can not choose date before today!");
    } 
}