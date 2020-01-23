# [Arrow functions, the basics](https://javascript.info/arrow-functions-basics)

## What have I learned? 
- Single line arrow functions are as follows: 
    - `let func = (arg1, arg2, ... argN) => expression;`
- Multi-line arrow functions require curly braces and a return statement: 
    
    ```JavaScript
    let func = (arg1, arg2, ... argN) => {
        return expression; 
    }
    ``` 

- When passing in arrow functions as arguments into another function, you don't need to re-declare a parameter after it's already been declared once. 

    ```JavaScript
    let age = prompt("What is your age?", 18);

    // arrow functions, note how let welcome only happens once....
    let welcome = (age < 18) ? 
        () => alert('Hello') : // If you were to remove the (age < 18) ? and part after the colon, then this would be a regular old arrow function. 
        () => alert("Greetings!"); // There are no parameters, so the parentheses are empty. 
    ```

## Notes 


- What are arrow functions?
    - Functions that accept arguments in parentheses and evaluate them in the expression to the right. 

- What syntax do they have? 
    - in general, without curly braces:
        
        ```JavaSCript
        let func = (arg1, arg2, ... argN) => expression; // note the '=>' which is an arrow, hence the name arrow function 
        ```
    - it's shorter than the below piece of code for Function Expressions

        ```JavaScript
        let func = (arg1, arg2, ... argN) => {
            return expression; 
        }; 
        ```

- What's a concrete example of the arrow function vs. the function expression? 

    ```JavaScript
    let sum = (a,b) => a + b; // arrow function is one line

    // function expression takes three line, requires the function word, and a return keyword... 
    let sum = function(a,b) {
        return a + b; 
    }
    
    alert( sum(1,2) ); // 3
    ``` 

- What are the minimum elements for an arrow function with only one argument or no arguments? 
    - `let double = n => n * 2;` has no need for parentheses with only one argument
    - with 0 arguments, use parentheses but they're empty. `let sayHi = () => alert("hello!"); sayHi();`

- Why use arrow functions? 
    - Can be used to dynamically create functions upon flow of execution
    - Useful for concise one-liners 
    - call backs
    - usually simpler and more concise syntax than function expressions/better

- How do we write multiline arrow functions? 
    - enclose expression in curly braces and add a return
    - e.g. 

        ```JavaScript
        let sum = (a,b) => { // curly braces
            let result = a + b;
            return result; // return is mandatory for curly brace arrow functions
        };

        alert( sum(1, 2) ); ) // 3

        ```

- What are the two types of arrow functions?
    - without curley braces
    - with curly braces

## Task
- Rewrite with arrow functions: Replace function expressions below with arrow functions in the code below:

```JavaScript 
function ask(question, yes, no) {
    if (confirm(question)) yes()
    else no(); 
}
```
- Replacement arrow function. 
    ```JavaScript
    ask = (question, yes, no) =>  {
        if (confirm(question)) yes() 
        else no(); 
        return; 
    }; 
    ``` 
    - Why did I do it this way? 
        - I think that for multi-line arrow expressions, the statements should be the same, but there needs to be an explicit `return`, hence the empty return. However, I'm not exactly sure... I also think that the syntax for the arrow function is that there is no need for the `function` keyword. The function name should be a variable, which is set to equal the parentheses with the parameters in between them. Then, the arrow function should point to the curly braces to show that the parameters are going to go into the function and be evaluated. 

```JavaScript
ask(
  "Do you agree?",
  function() { alert("You agreed."); },
  function() { alert("You canceled the execution."); }
);
```
    - Replacement arrow function 
   
    ```JavaScript
    ask( 
        "Do you agree?",
        let yes = () => alert( "You agreed."); ,
        let no = () => alert( " You canceled the execution." ); 
    ); 
    ``` 
    - Why did I do this? 
        - I think that the anonymous functions (Function Expressions) could be counted as single-line functions. Since they are single line functions that don't take a parameter, then there would just be empty parentheses. 


- **The solution given by the article:**

```JavaScript
function ask(question, yes, no) {
  if (confirm(question)) yes()
  else no();
}

ask(
  "Do you agree?",
  () => alert("You agreed."),
  () => alert("You canceled the execution.")
);
``` 

    - What's the difference between this function and what I just did? 
        - Well, they didn't rewrite the actual function declaration, just the function expression. Initially, I just had the () with empty parentheses, but thought I'd need to declare the variables. I guess, the declaration of the variable occurred in the function definition as a parameter. I also did not need to have the semi-colons with the function expressions, but instead should hav eused commas. Not sure, why. 




