# Functions

[JavaScript.info](https://javascript.info/function-basics)

- Functions cannot modify the variables defined within other functions because those variables are out of scope. However, functions can freely modify _global_ variables.

  - If a global variable `person` is declared and defined as `John Doe`, a function called `nameChange()` could set `person` to `Alan Watts` when run. Once `nameChange()` runs, the value of the global variable `person` changes from `John Doe` to `Alan Watts`.

  ```JavaScript
  let person = 'John Doe';

  function nameChange() {
      person = 'Alan Watts'; // Since there is no local variable called person, nameChange() will modify the global variable.
  }

  nameChange();
  console.log(person); // outputs 'Alan Watts'

  ```

- If a function declares a variable with the same name as a global variable, then the function will only modify its local variable and not affect the global variable.

  ```JavaScript
  let person = 'John Doe';

  function nameChange() {
      let person = 'Alan Watts'; // Declaring a local variable with the same name as the global variable inside a function won't cause the global variable to change when the function is run.
  }

  nameChange();
  console.log(person); // Outputs 'John Doe'
  ```

## Default Values

- What happens when a parameter is not provided to a function?
- How do you specify a default function in case no parameter gets passed?

## What does a function return when it has an empty `return` or has no `return`?

- `undefined`.

## What are some conventions for writing functions?

- Function names should be verbs and the function should start with a verb that relates to the action of the function. For instance, `"get..."` should return a value, `"calc..."` should calculate something.
- Each function should only do one thing, as per the name.
- Functions should be short and concise.
- Functions should act as comments/documentation.

## Practice

1. Rewrite the function using `?` or `||`: The following function returns `true` if the parameter `age` is greater than `18`. Otherwise, it asks for a confirmation and returns its ressult.

   ```JavaScript
   function checkAge(age) {
       if (age > 18) {
           return true;
       } else {
           return confirm ('Did parents allow you?');
       }
   }
   ```

   - Rewritten with `?`

   ```JavaScript
   function checkAge(age) {
       return ( age > 18 ) ? true : confirm('Did parents allow you?');

   }
   ```

   - Rewritten with `||`

   ```JavaScript
   function checkAge(age) {
       return ( age > 18 ) || confirm('Did parents allow you?');
   }

   ```

2. Function min(a,b): Write a function `min(a,b)` which returns the least of two numbers `a` and `b`.

   - My solution with `if`

   ```JavaScript
   function min(a,b) {
       if ( a  < b  || a == b ) {
           return a;
       } else {
           return b;
       }
   }
   ```

   - My solution with `?`

   ```JavaScript
   function min(a,b) {
       return ( a <=  b ) ? a : b
   }
   ```

   - Difference between my solution and the website solution?
     - I accounted for equality, but since the function is simply trying to return the _least_ of the numbers and it doesn't matter whether we return a or b if they're the same, then I don't need to account for that scenario.

3. Function power(x,n): Write function `pow(x,n)` that returns `x` in power `n`.

- Multiplies `x` by itself `n` times and returns the result.
- Make webpage that prompts for `x` and `n` and then displays result.
- Function should only support natural values 1+.

  - My `pow(x,n)` function

  ```JavaScript

  function pow(x,n) {
      return x**n;
  }
  // Prompt and display
  let x = prompt('What is the value of x?');
  let n = prompt('What is the value of n?');

  alert( pow(x,n) )
  ```

  - Revised function after realizing that a loop is called for

    ```JavaScript
      let x = prompt("What is the value of x?");
      let n = prompt("What is the value of n?");

      alert(pow(x, n));

      function pow(x,n) {
        if (n < 1) {
            alert("Not a natural number, refresh and try again.");
        } else {
            let i;
            let y = x;
            for ( i = 1; i < n; i++ ) {
                y = y * x;
            }
            return y;
        }
    ```

    - Solution

        ```JavaScript
        function pow(x, n) {
        let result = x;

        for (let i = 1; i < n; i++) {
            result *= x;
        }

        return result;
        }

        let x = prompt("x?", '');
        let n = prompt("n?", '');

        if (n < 1) {
        alert(`Power ${n} is not supported, use a positive integer`);
        } else {
        alert( pow(x, n) );
        }
        ``` 
        - The difference is that the function is defined first and the alert has the `${n}` is included to reflect the n that was input. The `i` was defined within the for loop and the result portion was made more concise with `*=` instead of `result = result * x;`. 