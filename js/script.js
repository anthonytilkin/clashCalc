// script.js

// Function to clear the calculator display
function clearDisplay() {
    document.getElementById('display').value = '';
  }
  
  // Function to append a value to the display
  function appendToDisplay(value) {
    document.getElementById('display').value += value;
  }
  
  // Function to evaluate the expression and display the result
  function calculateResult() {
    try {
      let result = eval(document.getElementById('display').value);
      document.getElementById('display').value = result;
    } catch (error) {
      alert("Invalid operation!");
    }
  }
  