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

[x] Goal: Create a calendar application with

- [x] `<select>` element to choose between different months: January - December
- `onchange` event handler to detect when value in `<select>` is changed
  - Write a conditional statement within above handler to:
    - check value of month stored in `choice` variable, the value of the `<select>` element after value changes, e.g. "January"
    - set value of `days` equal to # of days in each month
- `createCalendar()` function to draw calendar and display correct month in `<h1>` element

Some extra information:

- How many days are there per month?
  > 30 days hath September,
  > April, June and November,
  > All the rest have 31,
  > Excepting February alone
  > (And that has 28 days clear,
  - http://www.eudesign.com/mnems/dayspcm.htm
  - January - 31
  - February - 28
  - March - 31
  - April - 30
  - May - 31
  - June - 30
  - July - 31
  - August - 31
  - September - 30
  - October - 31
  - November - 30
  - December - 31
- What is the default # of days in a month? 
  - 31

- Based on the above, which conditions do I want to check for?
  - Whether a month is:
    - February
    - April, June, September, November


## Conditional Operators: if, '?' 

https://javascript.info/ifelse

1. Using the `if..else` construct, write the code which asks: 'What is the "official" name of JavaScript?'
    - If the visitor enters "ECMAScript", then output "Right!", otherwise output: "Didn't know? ECMASCript!"
    
    ```JavaScript
    let name = prompt('What is the "official" name of JavaScript?'); 

    if (name == 'ECMAScript') {
      alert("Right!"); 
    } else {
      alert("Didn't know? ECMAScript!"); 
    }
    ```

2. Show the sign. Using `if..else`, write the code which gets a number via `prompt` and then shows in `alert`: 
    - `1`, if the value is greater than zero, 
    - `-1`, if less than zero, 
    - `0`, if equals 0. 

    ```JavaScript
    let number = prompt("Input a number.");

    if (number > 0) {
      alert(1); 
    } else if (number < 0) {
      alert(0);
    } else {
      alert(-1); 
    }
    ```

3. Rewrite `if` into `?`: 
  - Original: 

    ```JavaScript
    let result; 
    
    if (a + b < 4) {
      result = 'Below';
    } else {
      result = 'Over';
    }
    ```

  - My answer Using `?`: 
    
    ```JavaScript
    let result; 

    (a + b < 4) ? result = 'Below' : result = 'Over'; 
    ```
  
  - Solution: 
    
    ```JavaScript
    let result = (a + b < 4) ? 'Below' : 'Over'; 
    ```   

4. Rewrite `if..else` using multiple ternary operators `?`. 

  - Original: 

    ```JavaScript
    let message; 

    if (login == 'Employee') {
      message = 'Hello'; 
    } else if (login == 'Director') {
      message = 'Greetings'; 
    } else if (login == '') {
      message = 'No login'; 
    } else {
      message = ''; 
    }
    ``` 

  - My rewritten solution == Same as solution!: 
    
    ```JavaScript
    let message = (login == 'Employee') ? 'Hello' : 
      (login == 'Director') ? 'Greetings' : 
      (login == '')         ? 'No login'  : 
      ''; 
    ``` 

## [How to Use the Switch Statement in JavaScript](https://www.digitalocean.com/community/tutorials/how-to-use-the-switch-statement-in-javascript)

