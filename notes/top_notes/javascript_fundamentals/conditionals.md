# Conditionals in JavaScript

- [Fundamentals Part 2](https://www.theodinproject.com/courses/web-development-101/lessons/fundamentals-part-2)

## [JavaScript if else and else if](https://www.w3schools.com/js/js_if_else.asp)

- Conditional statements:

  - `if`

    ```JavaScript
    if (condition) {
        // statements
    }
    ```

  - `else`

  ```JavaScript
  if (condition) {
    // statements run when condition is true
  } else {
    // statements run when condition is false
  }
  ```

  - `else if`

  ```Javascript
  if (condition1) {
    // statements
  } else if (condition2){
    // statements run if condition1 is false, but condition2 is true
  } else {
    // statements run if neither condition1 or condition2 are true
  }
  ```

## [Making decisions in your code -- conditionals](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/conditionals)

- How are `switch` statements useful?

  - They reduce the amount of code you need to write when you have a lot of choices, esp. when those choices don't need much code (e.g. changing the value of a variable).

- What is the syntax of the `switch` statement?

  ```JavaScript
  switch(option) {
    case '1':
      // action 1
      break;
    case '2':
      // action 2
      break;
    case '...':
      // action ...
      break;
    case 'n' :
      // action n
      break;
    default:
      // default action
  }
  ```

  - Begins with `switch(option)`
  - Each option is represented by `case 'option':`
  - The action to run is indented below it with a `break;` on another line to skip the rest of the options.
  - There is an optional `default:` in case there are unexpected values input for option.

- What is the ternary (AKA conditional) operator?

  - Code that tests a condition and returns one value/expression when it's `true` and another when it's `false`.

  ```JavaScript
  ( condition ) ? 'run this code' : 'run this code instead'
  ```
  
  - e.g.
  
  ```JavaScript
  let greeting = ( isBirthday ) ? 'Happy birthday Mrs. Smith - we hope you have a great day!' : 'Good morning Mrs. Smith.';
  ```
  

### Active Learning: A Simple Calendar
