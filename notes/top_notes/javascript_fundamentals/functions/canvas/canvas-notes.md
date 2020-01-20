# HTML Canvas

[Reference](https://www.w3schools.com/tags/ref_canvas.asp)

## Why am I trying to learn about this?

I was working on the [function return values](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Return_values) article from Mozilla and I found myself confused as to what the [random-canvas-circles-html](https://github.com/mdn/learning-area/blob/master/javascript/building-blocks/loops/random-canvas-circles.html) example was doing. First, I tried to play around with the variables and figure out what each line was doing, but then I hit a block and still felt like there were gaps in my understanding, so I wanted to check out what the methods were doing.

After doing some experimentation, I was still curious about:

- What exactly is the canvas element?
- What does `getContext` do?
- What does `clearRect` do?
- What does `beginPath()` do? Why do we need it to prevent the draw function from filling in the space between circles?
- What do the fourth and fifth parameters of `ctx.arc(random(WIDTH), random(HEIGHT), random(50), 0, 2 * Math.PI);` do?

## Canvas Element

- What is the canvas element?
  - It's an HTML5 element whose purpose is to contain drawings made via JavaScript.

### `getContext()`

- What does `getContext()` do?
  - `getContext()` is a method that instantiates an object that can draw on the canvas.
  - `getContext("2d")` instantiates an object used to make two-dimensional drawings.

### `clearRect()`

- What is the syntax?

  - `context.clearRect(x, y, width, height);`

  ```JavaScript
  var c = document.getElementById("myCanvas");
  // Instantiate an object called `ctx` that will have methods and properties for drawing two-dimensional objects.
  var ctx = c.getContext("2d");
  // Set the color that the fill() method will default to
  ctx.fillStyle = "red";
  // Beginning from the top-left corner of the canvas, fill in a rectangle of 300 pixels in width and 150 pixels in height with the color red.
  ctx.fillRect(0, 0, 300, 150);
  // Beginning 20 pixels to the right and 20 pixels down from the top-left corner of the canvas, revert the red coloring back to white for a rectangle of 100 pixels in width and 50 pixels in height.
  ctx.clearRect(20, 20, 100, 50);
  ```

- What does `clearRect()` do?
  - Within a specified rectangle, revert the pixels back to white.

### `beginPath()`

- What is the syntax?

  ```JavaScript
  context.beginPath();
  ```

- What does `beginPath()` do? Why do we need it to prevent the draw function from filling in the space between circles?
  - It tells the computer that we are starting to draw a shape, and that if we already finished drawing a shape, we are starting anew. Without beginPath(), the computer would still think that we're drawing the same shape. That is, when we try to draw three circles one after another and fill in the circles with black ... the computer thinks we're actually trying to fill in the circles with black AND the space between them too because it doesn't realize that the circles are separate shapes.

### `context.arc()`

- What is the syntax?

  ```JavaScript
  context.arc(x, y, radius, startingAngle, endingAngle, optionalDirection);
  // The optional direction defaults to drawing the circle in a clock-wise direction, with 0 starting at eastern direction and moving south, west, north, and back to west. Counter-clockwise starts at west and moves north, west, south, east.
  ```

- What do the fourth and fifth parameters of `ctx.arc(random(WIDTH), random(HEIGHT), random(50), 0, 2 * Math.PI);` do?
  - The fourth and fifth parameters determine the starting and ending angles of the circle. If you set starting angle at 0, then the circle will be drawn from the Western point and then draw in a clockwise direction until it reaches the ending angle... in radians. Therefore, beginning at `0.5 * Math.PI` should start at the 6 o' clock position and end back at the 3 o'clock position. 
    - If you don't fill the circle and just have a line, then it'll miss the curve between the 3 o clock and 6 o clock position. If you fill the circle, then there will be a diagonal line from the 3 o clock to the 6 o clock position. 