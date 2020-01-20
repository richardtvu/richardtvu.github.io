# [Function return values](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Return_values)

## Learning Objectives

- What do you need to understand about function return values?
  - Return values are the outputs that functions produce when run. Often, these return values are used as intermediary steps in calculations.
- How do you make use of function return values?
  - You can pass in the return values as parameters into other functions.
  - You can store the return values in variables outside of the function scope it was defined in, allowing for use of that value outside the function.

### What are return values?

- **Return values** are the outputs of functions that can be stored into variables, used by other functions as parameters, etc. They are values output by functions.
  - Not all functions return values. Instead, they return `void` or `undefined`.
    - e.g. `displayMessage()`
- Functions with return values are generally used as intermediate steps in calculations.

### How do you use return values in your own functions?

- Include `return` followed by the variable/value/expression to be returned in the fucntion definition.

### Active learning: Creating our own return value function?

- What did you do in this active learning exercise?
  - Created a local copy of the [function-library.html](https://github.com/mdn/learning-area/blob/master/javascript/building-blocks/functions/function-library.html) file from Github.
  - Copied down the functions and event handler code to the local copy.
- What did you learn from the exercise?
  - You can have the variable and the values/strings on different lines of code.
  - The `onchange` event handler when used with a text box can register changes after the tab or enter key is pressed.

### Exploration time: Creating some functions of your own and adding them to the library

- How do you get the square or cube root of the number?
- How do you get the circumference of a circle with a given radius?
- Can you write some _error handling_ into the functions to check that the parameters are validated and that optional parameters have some kind of default value?
- What kind of functions might you use over and over again, thereby warranting inclusion in your own _function library_?
