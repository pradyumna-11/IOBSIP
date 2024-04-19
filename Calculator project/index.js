let resultElement = document.getElementById("resultElement");

let string = "";

function check(no) {
  string = string + no;
  resultElement.textContent = string;
}

function calculate(op) {
  string = string + op;
  resultElement.textContent = string;
}

let result = "";

function clickedResult(op) {
  result = eval(string);
  console.log(typeof result);
  string = result.toString();
  resultElement.textContent = result;
}

function clickedSingleClear() {
  string = string.slice(0, string.length - 1);
  resultElement.textContent = string;
}

function clickedClear() {
  string = "";
  resultElement.textContent = 0;
}
