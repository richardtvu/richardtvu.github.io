# Functions -- reusable blocks of code

[MDN](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Functions)

## Learning Objective:

- What are the fundamental concepts behind JavaScript functions?

  - What is the basic syntax of functions?

    ```JavaScript
    function [functioname]() {
      // code goes here
    }
    ```

  - How do you invoke functions?

    ```JavaScript
    [functionname](parameters-if-needed);
    ```

  - What is scope?

    - The box that defines which functions can access which variables. The global scope is the box containing all functions, so any variables defined in the global scope can be accessed by all functions. The local scope is the box defining variables for a specific function, so only functions within that box can access those variables.

  - What are parameters?
    - The variables, expressions, values, etc. that are passed into a function to let it do its job.

## Functions in General

- What is the function of functions (pun intended)? I.e. Why might you use functions?
  - Functions let you store a block of code that is easily-called by a short command. Thus, by using functions, you can re-use old code and cut down on the code you use in the future, whilst also avoiding reinvention of the wheel.
- Where can you find functions?
  - Functions can be found beyond the built-in features of a language (e.g. loops, if...else statements) as the commands using parentheses `()`.
- What are some built-in functions of JavaScript?

  - String manipulation, e.g. `[variable].replace('string-to-be-replaced', 'replacement-string')`, e.g.

    ```JavaScript
    let myName = 'Johnny Vu';
    let myActualName = myName.replace('Johnny', 'Richard');
    console.log(myActualName);
    // prints 'Richard Vu' after taking myName and replacing 'Johnny' with 'Richard'
    ```

  - Array manipulation, e.g. Combining all of the items in an array together into a single string with a space between the items.

    ```JavaScript
    let fragments = ['Jordan', 'Peterson', 'is', 'my', 'hero'];
    let wholeSentence = fragments.join(' ');
    console.log(wholeSentence);
    // Combines the items of fragments into the whole sentence, "Jordan Peterson is my hero"
    ```
    
  - Random number generation.

- What does it mean to **invoke** a function?
  - To **invoke** a function is to run that function or execute it.
  - Use the function name with parentheses. to invoke it.

### Functions vs. Methods

- What is the difference between functions and methods?
  - Methods are functions, but functions are not necessarily methods.
    - A square is a rectangle, but a rectangle is not necessarily a square.
- What are **methods**?
  - Methods are functions that are part of objects. Objects are programming entities that have behaviors/actions, **methods**.
- What are **custom functions**?
  - **Custom functions** are functions that you or someone else have written in the code instead of being built-in to the browser.

### Anonymous functions

- What are anonymous functions?

  - **Anonymous functions** are functions without names.

    ```JavaScript
    // Named function
    function myFunction() {
        alert('hello');
    }
    // Anonymous function
    function() {
        alert('hello');
    }
    ```

- What are the uses of anonymous functions?

  - Used in conjunction with event handlers to run a block of code whenever a particular event happens, e.g. clicks of a button.

  ```JavaScript
  const myButton = document.querySelector('button');

  myButton.onclick = function() {
      alert('hello');
      // a whole bunch of code
      // as much as I want...
  }
  ```

### Parameters

- What are **function parameters**?

  - Values that help the function do something... like where a math function begins its calculations. Some functions require parameters, others don't.
  - The ones that don't probably already have the necessary values to run: e.g. the `Math.random()` function will generate a number between 0 and 1, which can be specified in the function itself.

    ```JavaScript
    console.log(Math.random());
    // e.g. 0.05918726975275068
    ```

  - Some that do, might need a single parameter, two parameters, or a whole bunch... Sometimes those parameters are _optional_, but that's because the function will use some actions by default.

### Scope and Conflicts

- What is function scope?
  - **scope** is like a box. When variables and values, or even functions, are defined within a function, they are placed within a box. So only function in which those values/variables were defined will have access to use those variables and values. That's _local_ scope.
  - By contrast, **global scope** is the mega box for the entire program. Any variables/values and functions defined here can be used by other functions anywhere in the program.
- What is the purpose of scope?
  - Compartamentalize functions and values, so that external scripts or even the functions withiin the code don't mess shit up.
- How can there be conflicts in scope? How can conflicts arise?
  - When a variable is already declared in an external JavaScript, trying to declare it again in another script will throw an error. Scope is like a zoo. The global scope is the zoo keeper with access to all of the cages. You don't want the tigers and other predators to get out because they might eat the other animals or just be plain bad.

### Active learning: Playing with Scopes

- What did you do to actively learn about functions?
  - Copied the function-scope html example from MDN.
  - Opened up the example in browser and tried to display variables x, y, and z. Only x was output to the screen because the other variables were only defined within their functions, in **local scope**. Thus, they were inaccessible to the console, which was trying to accesss those values from global scope.
  - Edited the functions to call the `output()` function from within the `a()` and `b()` functions, which resulted in successfully displaying the values of y and z on the web page. The `output()` was defined in global scope and so was accessible to `a()` and `b()`.
  - Edited two `a` and `b` functions to call `output(x)`, which resulted in displaying 1 on the webpage both times. This confirms that `x` is accessible from within these functions because `x` was defined within global scope.
  - Edited `a` to call `output(z)` and `b` to call `output(y)`. Got a reference error for both function calls because they are trying to print variables not defined within the same function scopes.
- What did you learn from the active learning task?
  - Functions can use variables that are defined with the **global scope** or variables defined within their **local scope**, but they cannot use variables defined with the **scope** of other functions.

### Functions inside functions

- Why might you nest a function inside another function?
  - Breaking down a function into smaller sub-functions, you make the code easier to read and more organized. You also make it easier to re-use functions, combine them in different ways, etc. This is the idea of "de-coupling", that is, making components less dependent on each other, so that you can make changes to sub-components without affecting the other components.
- What are some problems that can arise from nesting functions?

  - If you try to use a variable in a nested function, then that variable needs to be ported into the nested function as a parameter from the supra-function ... because the code for that sub-function will look for the variable within the sub-function definition.
  - The following will be an example of code that will throw a reference error vs. code that won't throw a reference error because the value of interest will be ported into the sub-function.

    ```JavaScript
    // Reference Error! The variables of interest are defined within the same scope as the function call, but is not defined within the function being called, so the  sub-function doesn't know what to output!
    function printFavoritePerson() {
      let heroTitle = 'Dr.';
      let heroFirstName = 'Jordan';
      let heroLastName = 'Peterson';

      printTitle()';
      printFirstName();
      printLastName();
    }

    function printTitle() {
      console.log(heroTitle);
    }

    function printFirstName() {
      console.log(heroFirstName);
    }

    function printLastNme() {
      console.log(heroLastName);
    }

    // Good! No Reference error! The variables of interest are both defined within the same scope of the function call **and** also defined within the sub-function because they were passed in as parameters. Thus, the sub-functions can know the the values of the variables and properly output them.
    function printFavoritePerson() {
      let heroTitle = 'Dr.';
      let heroFirstName = 'Jordan';
      let heroLastName = 'Peterson';

      printTitle(heroTitle)';
      printFirstName(heroFirstName);
      printLastName(herolastName);
    }

    function printTitle(value) {
      console.log(heroTitle);
    }

    function printFirstName(value) {
      console.log(heroFirstName);
    }

    function printLastNme(value) {
      console.log(heroLastName);
    }

    ```

### Conclusion:

- What are the fundamental concepts behind functions?
  - Functions let use encapsulate blocks of code into a short command that makes it easier to reuse code and easier to read too, if done properly.
  - Breaking down functions into sub-components help make functions more readable. However, you must be careful to make sure that parameters are passed into sub-functions, otherwise the sub-functions will treat the parameters of interest as being undefined... even though they're in the same scope.
  - Functions can use variables defined in their **local scope**, that is within their definition, and variables defined in the **global scope**, which are accessible to all functions. However, functions cannot use variables defined in other functions... unless those functions return those variables and pass those into the function of interest as parameters.
