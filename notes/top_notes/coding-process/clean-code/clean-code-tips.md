# How do you keep your programming code clean?

- [Keeping Your Programming Code Clean](https://onextrapixel.com/10-principles-for-keeping-your-programming-code-clean/)

1. Get the logic down pat _before_ you code. Because ...
    - It'll help prevent huge functions and lots of rewriting and refactoring of code 

2. Label the structure of the page...

   - with an ID so that it's clear what the container is supposed to contain.

3. Use correct indentation

   - instead of having everything be to the left.

4. Write Explanatory comments.

5. Avoid Abusing Comments.
   - How do you avoid abusing comments? Refrain from using comments to:
     - make notes to self, `e.g. /* Finish this later */`
     - blame others
     - write vague statements, e.g. `/* this is a math function */`
     - erase code ... without following up on it and then either removing that comment + code or modding code to not need the comments
   - How do you use comments well? By
     - Documenting the author, e.g. `/* Coded by Rich, January 25, 2020 */`
     - Providing detailed explanations on what a method or procedure does, **NEEDS AN EXAMPLE OF MY OWN**
     - Using them as notifications/labels to mark recent changes, e.g. `/* Refactored code to decompose login-validation function into two separate functions */`

6. Avoid Huge Functions. 
    - Decompose big functions into smaller functions. 

7. Use Naming Standards for Functions and Variables.

8. Ensure Changes Made to Code Adhere to Clean Code Standards: 
    - Maintain correct indentation. 
    - Comment to explain mods / expand existing comments
    - Adhere to standards in use. 

9. Minimize Mixing of Coding Languages because ...
    - The flow of structure will get interrupted and therefore 
    - the code will be harder to read 

10. Summarize Your Imports 
    - Keep style sheets to a maximum of one or two instead of importing a lot of style sheets because ...
        - It'll make the code more organized and easy to read
        - reduce loading time and be more efficient 

## To Sum Up

- The best development process involves lots of little things that make the short-term development longer and harder, but ultimately makes long-term development easier, more efficient, and effective.

- Whiteboard / flow chart your program logic, use the pseudo-code programming process too to make sure you know the purpose of the program and the pieces needed to make the program work. Doing that will help minimize unnecessary rewriting of code, unnecessarily large functions because you'll have decomposed them. Once you've started, keep your indentation and styling consistent, make sure that the structure of the page is clear with IDs or using the HTML5 main tags together with the IDs. Separate programming languages. Minimize the imports to promote organization and performance. Keep comments to things that directly explain the functionality of methods/procedures, to things like authoring specs, to explaining recent changes, etc. Refrain from commenting as a way to remind yourself of what to do, to blame others, etc. basically things that aren't useful in understanding the code. Use the comments to make sure that code is understandable. 
