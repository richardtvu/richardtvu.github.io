const btn = document.querySelector("button");
const canvas = document.querySelector("canvas");
// Generates an object that can draw 2d images on top of the canvas
const ctx = canvas.getContext("2d");

// Get the WIDTH of the web page when the page is first loaded.
let WIDTH = document.documentElement.clientWidth;
// Get the HEIGHT of the web page when it is first loaded.
let HEIGHT = document.documentElement.clientHeight;

// Set the width of the canvas to the WIDTH of the webpage when it's first loaded.
canvas.width = WIDTH;
// Set the height of the canvas to the WIDTH of the webpage when it's first loaded.
canvas.height = HEIGHT; 

function random(number) {
  // Step 1. Generate a random number between 0 and 1.
  // Step 2. Multiply that result by the upper limit passed in as the parameter, number. (e.g. 10) to produce a number between 0 and 10, exclusive.
  // Step 3. Floor the result, as in take only the first number and disregard any trailing decimals. e.g. if the result is 9.7854781723, then the final result will be 9.
  // Step 4. Return that number.
  return Math.floor(Math.random() * number);
}

// Clear out the pixels on the web page and draw 100  new circles each time a click of the "button" occurrs. 
function draw() {
  // Clear all the pixels in the webpage, so that the previous circles are gone when we draw the next 100 circles. 
  ctx.clearRect(0, 0, WIDTH, HEIGHT);

  // Generate 
  for (let i = 0; i < 100; i++) {
    // Reset the path, so that each circle will be treated as a different one. This prevents the fill() method from coloring in the space between circles. 
    ctx.beginPath();
    // Set default fill() color to red at half opacity. 
    ctx.fillStyle = "rgba(255,0,0,0.5)";
    // Make a circle whose position is randomly set along with the width and height of the page with a random radius up to, but not including 50 pixels. Draw the circle starting from the 3 o clock position in a clockwise direction and end back up at the 3 o clock position. 
    ctx.arc(random(WIDTH), random(HEIGHT), random(50), 0, 2 * Math.PI);
    // Colors in the circle based on the fillStyle. 
    // Color in the circle as red. 
    ctx.fill();
  }
}

// Whenever the button is clicked, run the draw() function. 
btn.addEventListener("click", draw);
