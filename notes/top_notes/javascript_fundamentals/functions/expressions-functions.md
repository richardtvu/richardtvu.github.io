# [Function expressions](https://javascript.info/function-expressions)

- What are the differences between a _function declaration_ and a _function expression_?
  - Function declarations are processed outside of the normal flow of code, but function expressions are processed as the flow of execution reaches them.
  - Function Expressions are stored in variables.
    - Because Function Expressions are used inside statements, they need a semi-colon as per normal convention for statements.
- You can only call a function expression at or after the time of declaration, but function declarations can be called at any time, even before definition. This is because function expressions are only created upon the flow of execution reaching them. 

- Why are function expressions useful?
    - They let you ... make the code more concise. 
    - They let you call from outside a code block a function that you've defined within that code block. By contrast, if you define a code dec. inside an `if` block, then you can't call that function outside the block. 

        ```JavaScript
        let age = prompt("What is your age?", 18); 

        let welcome;

        if (age < 18) {

        welcome = function() {
            alert("Hello!");
        };

        } else {

        welcome = function() {
            alert("Greetings!");
        };

        }

        welcome(); // ok now
        
        // Simpler version
        let welcome = (age<18) ?
            function() { alert("Hello!"); } :
            function() { alert("Greetings!"); };

        welcome(); 

        ```

- Why is there a semicolon `;` at the end of the function expression, but not the declaration?
- What are **callback functions**? Why are they useful?
- How do you choose between using a function declaration vs. a function expression?
  - In most cases, you should use function declarations because they are more visible, more flexible in terms of organizing code, more readable.
  - When should you instead use a function expression?
    - when we want a _conditional_ declaration, which is?

* What is an example of a function expression?

  ```JavaScript
  function ask(question, yes, no) {
      if (confirm(question)) yes()
      else no();
  }

  ask(
      "Do you agree?",
      function() { alert("You agreed."); },
      function() { alert("You canceled the execution."); }
  );
  ```

  ```JavaScript
  let sum = function(a,b) {
      return a + b;
  };
  ```

