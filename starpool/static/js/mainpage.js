function s1bt() {
  var s1Div = document.getElementById("s1");
  var s1Text = s1Div.querySelector("a");
  s1Div.style.backgroundColor = "#0F254E";
  s1Text.style.color = "white";
}

function buttonClick(buttonId) {
  var buttons = document.querySelectorAll(".button");

  for (var i = 0; i < buttons.length; i++) {
    var button = buttons[i];
    var buttonText = button.querySelector("a");

    if (button.id === buttonId) {
      button.style.backgroundColor = "#0F254E";
      buttonText.style.color = "white";
    } else {
      button.style.backgroundColor = "";
      buttonText.style.color = "";
    }
  }
}
