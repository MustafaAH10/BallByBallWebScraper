var menu1 = document.createElement("select");
var menu2 = document.createElement("select");

var option1 = document.createElement("option");
option1.value = "option1";
option1.text = "Option 1";
menu1.add(option1);

var option2 = document.createElement("option");
option2.value = "option2";
option2.text = "Option 2";
menu1.add(option2);

var option3 = document.createElement("option");
option3.value = "option3";
option3.text = "Option 3";
menu2.add(option3);

var option4 = document.createElement("option");
option4.value = "option4";
option4.text = "Option 4";
menu2.add(option4);

document.body.appendChild(menu1);
document.body.appendChild(menu2);

menu1.addEventListener("change", function() {
  var selection1 = menu1.options[menu1.selectedIndex].value;
  var selection2 = menu2.options[menu2.selectedIndex].value;
  alert("You selected: " + selection1 + ", " + selection2);
});
