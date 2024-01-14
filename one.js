function newElement() {
    var inputValue = document.getElementById("myInput").value;
    if (inputValue === '') {
        alert("You must write something!");
        return;
    }

    // Create a new list item
    var li = document.createElement("li");

    // Create elements for the checkbox and text input
    var checkboxDiv = document.createElement("div");
    checkboxDiv.className = "input-group mb-3";

    var checkboxInputGroupText = document.createElement("div");
    checkboxInputGroupText.className = "input-group-text";

    var checkboxInput = document.createElement("input");
    checkboxInput.className = "form-check-input mt-0";
    checkboxInput.type = "checkbox";
    checkboxInput.value = "";
    checkboxInput.setAttribute("aria-label", "Checkbox for following text input");

    var textInput = document.createElement("input");
    textInput.className = "form-control";
    textInput.type = "text";
    textInput.setAttribute("aria-label", "Text input with checkbox");
    textInput.value = inputValue;

    // Append the checkbox and text input to the checkboxDiv
    checkboxInputGroupText.appendChild(checkboxInput);
    checkboxDiv.appendChild(checkboxInputGroupText);
    checkboxDiv.appendChild(textInput);

    // Append the checkboxDiv to the list item
    li.appendChild(checkboxDiv);

    // Find the checked box and add the new item after it
    var checkedBox = document.querySelector('ul input[type="checkbox"]:checked');
    if (checkedBox) {
        // If a checked box is found, insert the new item after it
        checkedBox.closest('li').insertAdjacentElement('afterend', li);
    } else {
        // If no checkbox is checked, add the new item to the end of the list
        document.getElementById("myUL").appendChild(li);
    }

    // Clear the input
    document.getElementById("myInput").value = "";
}



