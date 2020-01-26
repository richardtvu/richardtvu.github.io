# [Writing Clean Code](https://www.theodinproject.com/courses/web-development-101/lessons/clean-code)

## Why write clean code?

- Developer **read more** code than they write, including the code they write themselves. Clean code will help developers better understand and intuit the what and why of the code much more effectively and faster than ugly, hard-to-read code.

  - This also applies to your own code.

- Clean code directly results in better use, maintenance, and development of existing code.

## What makes for clean code?

- **consistency**

- **self-explanatory** code:

  - descriptive function and variable names

## Rules of thumb?

1. Indentation: 2 spaces for indentation

2. Semicolons, to prevent code from breaking in edge cases.

3. Line length: Limit the length to make it easier to read.

   - Break the line:

     - around ~80 characters,
     - immediately _after_ an operator or comma

   - Indent second line **twice**.

4. Naming things:
   - Use **descriptive** names for functions and variables.
   - Always use camelCase.
   - Start _functions_ with a verb.
   - Start _variables_ with a noun.
   - Avoid single character variable names, except in loops or callback functions.

## Assignments

1. [List of clean-code tips](https://onextrapixel.com/10-principles-for-keeping-your-programming-code-clean/)

   - How do you keep your code clean?
     - Map out the logic, purpose, and structure of the program _before_ coding.
     - Label and organize structure of page clearly, with identifiers (in tags), appropriate indentation, and line-breaks.
     - Decompose functions to the simplest units available, to avoid huge functions.
     - Simplify all code and make them as self-documenting as possible _before_ commenting.
     - When commenting,
       - make sure that the comments are either for
         1. author specifications,
         2. explaining the _why_ of the code or providing _specific_ and detailed explanations on what the method does, or
         3. documenting recent changes to code or expanding existing comments.
       - refrain from using comments as
         - notes to self
         - ways to blame others
         - ways to remove code from compiler execution _without_ following up on and removing the code or modding code to not need comments
         - vague explanations of what the code does
     - Separate coding languages and
       - keep imports to a minimum, i.e. 1 or 2 style sheets instead of 3+ to maintain efficiency and performance of code

2. What is the role of comments in your code?

   - [Coding without comments](https://blog.codinghorror.com/coding-without-comments/).

     - Excessive comments are the lazy way of making code understandable. More often, the code itself is just bad and should be refactored, rewritten, or rearchitect-ed. Simple, clear, self-documenting code is the mark of a senior developer. By contrast, the mark of a junior developer is a reliance on comments as a crutch to explain their code.
     - The purpose of comments is to communicate with human beings, but most people who got into coding are horrible writers (including me). Thus, focus on the strength of writing good code that will do a better job of communicating.

   - [Code tells you how, comments tell you why](https://blog.codinghorror.com/code-tells-you-how-comments-tell-you-why/)

     - Comments provide the *context* of **why** a method for doing something was chosen over other methods, whereas the how something will be done should be understood through the code. When writing code, the programmer should keep in mind that their audience is other humans and therefore should re-factor, re-write their code to become as simple and easy to understood as possible *before* adding comments, lest the code become messy and opaque. 

## Additional Resources

- [Code as documentation](https://www.martinfowler.com/bliki/CodeAsDocumentation.html)
    - Code is the most up-to-date, reviewed and typically most-accurate form of documentation. However, without effort to make code simple and easy-to-read, code is a poor form of documentation. To make the most use of code, get as much feedback as you can via code reviews, pair programming, etc. and re-factoring to make code understandable to others. 

- [Complete guide to self-documenting guide](http://wiki.c2.com/?SelfDocumentingCode)

- [Airbnb style guide](https://github.com/airbnb/javascript)

- [Chaining methods to write sentences](http://javascriptissexy.com/beautiful-javascript-easily-create-chainable-cascading-methods-for-expressiveness/)
