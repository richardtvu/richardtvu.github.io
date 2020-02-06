# Loops

- [TOP](https://www.theodinproject.com/courses/web-development-101/lessons/fundamentals-part-4?ref=lnav)

## Summary

- What are loops useful for?

## [Looping code](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Looping_code)

### Summary

- Why are loop structures important? - What are the different types of loops and when should you use them?

  - Useful for quickly repeating the same actions, so you don't have to write them out over and over.

- What'd you practice in the MDN [loop test](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Test_your_skills:_Loops)? How?

### Questions

- What are loops?

  - coding structures

- What features do loops have?

  - `for ( )` to signifiy the for loop
  - up to three parameters to set for loop behavior

    - `initializer` - initiation / counter variable
    - `exit condition` - end condition, the condition that stops looping and continues with the code
    - `final-expression` - iterator / code that runs after each full loop

  - `{ block of code }` - the statements to run each loop

- Why use loops?

  - To repeat the same actions multiple times without having to write out those actions over and over...

- What's the standard `for` loop?

  ```javascript
  let i; //variable to hold the current iteration of the loop 
    let maxLength = 20; // e.g. you want to run 20 loops
    for (i = 0; i < maxLength; i++) {
        // statements
    }
  ```

- How do you exit loops before all the iterations have been completed?

  - `break`

- How do you skip iterations?

  -`continue` ?

- What are the `while` and the `do ... while` loops?

  - Syntax:

    ```javascript
    initializer
      while (exit-condition) {
        // statements

        final-expression
      }
    ```

  - Rewrite the cats list example to use a while loop. 
    - Cats list example `for`
      ```JavaScript
      for (let i = 0; i < cats.length; i++) {
        if (i === cats.length - 1) {
          info += 'and ' + cats[i] + '.';
        } else {
          info += cats[i] + ', ';
        }
      }
      ```
    - `while` re-written
      ```JavaScript 
      let i = 0; 
      while (i < cats.length) {
        if (i === cats.length - 1) {
          info += 'and ' + cats[i] + '.';
        } else {
          info += cats[i] + ', ';
        }
        i++;
      }

      
- How do you choose which loop type to use?

### Active learning: Launch countdown! How do you print a simple launch countdown to the output box from 10 to Blastoff?

### Active learning: Filling in a guest list. How do you take a list of names stored in an array and put them in a guest list?

## [JavaScript.info](http://javascript.info/while-for)

- What kind of syntax does the `while` loop have?

- What's the syntax for the "do...while" loop?

- What's the syntax for the `for` loop?

- What is an "inline" variable declaration?

- Which parts of the `for` loop can be skipped?

- When should you use a `break`?

- When should you use a `continue`? Why might you use a `continue`?

- Can you use `break/continue` with the ternary `?` operator?

- How do we break out from multiple nested loops?

### Last loop value

1. What is the last value alerted by this code? Why?

  ```javascript
  let i = 3; 
  while (i) {
  alert( i-- );
  // alert 2 
  // alert 1
  // alert 0, but now i = 0, so loop ends 
  //  
  }`
  ```

2. Which values does the while loop show? For every loop iteration, write down which value it outputs and then compare it with the solution.

  - Both loops `alert` the same values, or not?

  - The prefix form `++i`:

    ```javascript
    let i = 0; 
    while (++i < 5) alert ( i );
    ```

  - The postfix form i++;

    ```javascript
    let i = 0; 
    while (i++ <5) alert ( i );
    ```

3. Which values get shown by the `for` loop?

  - For each loop write down which values it is going to show. Then compare the answer. Both loops `alert` same values or not?

  - The postfix form:

    ```javascript
    for (let i = 0; i < 5; i++) {
    alert( i ); 
    }
    ```

  - The prefix form:

    ```javascript
    for (let i = 0; i < 5;  ++i {
    alert( i );
    }
    ```

4. Output even numbers in the loop:

  - Use the `for` loop to output even numbers from `2` to `10`.

  - increment i by 2, starting from 2

    ```javascript
    for (let i = 2; i < 11; i += 2) {
    console.log(i); 
    }
    ```

  - increment i by 1, starting from 2

    ```javascript
    for (let i = 2; i < 11; i++ ) { 
    if (i % 2 == 0) {
    console.log(i); 
    } else {
    continue; 
    }
    }
    ```

  - increment i by 0, starting from 0

    ```javascript
    for (let i = 0; i < 11; i++) {
    if ( (i > 0) && (i % 2 == 0)) {
    console.log(i);
    } else {
    continue; 
    }
    }
    ```

    - The solution from the page

      ```javascript
      for (let i = 2; i <= 10; i++) {
      if (i % 2 == 0) {
       alert( i ); // show i if it can be divided by two without a remainder
      }
      }
      ```

      - The difference between this and my solution is that I'm using console.log instead of alert and that I'm including a `continue` when it's probably not necessary. I also don't use a `<=` as I favor the `<`.

5. Replace `for` with `while`. Rewrite the code changing the `for` loop to `while` without altering its behavior (the output should stay the same).

  ```javascript
  for (let i = 0; i < 3; i ++) {
  alert( `number ${i}!` ); 
  }
  ```

  Rewritten:

6. Repeat until the input is correct.

  - Write a loop which prompts for a number greater than `100`. If the visitor enters another number -- ask them to input again.

  - The loop must ask for a number until either the visitor enters a number greater than `100` or cancels the input/enters an empty line.

  - Assume that the visitor only inputs numbers. There's no need to implement a special handling for a non-numeric input in this task.

    ```javascript
    let visitorNumber = prompt("Input number greater than 100");

    askNumber(visitorNumber);

    function askNumber (visitorNumber) {
    while (visitorNumber <= 100 ) {
     askNumber(prompt("Try again. Input a number greater than 100")); 
    }
    return alert("Thank you. That number is greater than 100."); 
    }
    ```

  - Next step: Add in the code that will test for escape/exiting the input box/enters an empty line.

7. Output prime numbers:

  - An integer number greater than `1` is called a prime if it cannot be divided without a remainder by anything except `1` and itself.

  - In other words, `n > 1` is a prime if it can't be evenly divided by anything except `1` and `n`.

  - For example, `5` is a prime, because it cannot be divided without a remainder by `2`, `3`, and `4`.

  - **Write the code which outputs prime numbers in the internal from `2` to `n`**.

  - For `n = 10`, the result will be `2, 3, 5, 7`. The code should work for any `n`, not be hard-coded for any fixed value.

    ```javascript
    outputPrimesBetween(2, 10); // result should be 2, 3, 5, 7 

    function outputPrimesBetween(firstNumber, lastNumber) {
    let primes = []; 

    for (let number = firstNumber; number <=lastNumber; number ++) {
        if (isPrime(number)) {
            primes.push(number); 
        }
    }

    return primes; 
    }

    function isPrime(number) {
    // return false is the number can be divided by a number between 2 and the number itself 
    for ( let divisor = 2; divisor < number; divisor ++) {
        if (number % divisor == 0) {
            return false; // it's not a prime 
        }
    }       
    return true;
    }
    ```
