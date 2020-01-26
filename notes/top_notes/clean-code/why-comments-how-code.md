# [Code Tells You How, Comments Tell You Why](https://blog.codinghorror.com/code-tells-you-how-comments-tell-you-why/)

- When should you add comments to code? 
    - Only *after* you've exhausted opportunities to make code simpler to understand through re-writing and re-factoring code

- Who is your audience when you're writing code? 
    - Other people, so write code that *humans* can read and understand 
    - When we are writing code, we are trying to explain to another person (i.e. a teammate, you in the future, etc) what you want the computer to do.

- Why might you want to have *less* comments? 
    - Comments for insufficiently-revised code will make the code *harder* to read and understand. 

- How do you minimize unnecessary comments? 
    - Write code that is meant for a human audience. 
    - Refactor and re-write that code to be as simple as possible before adding comments. 
        - Choose meaningful variable and function names. 

- Why are comments still necessary when you want to write self-explanatory code? 
    - Code can explain the *how* of what a program is supposed to do, but it cannot explain **why** the programmers used a particular method for doing something. 
    - Comments provide the context, rationale for using certain approaches, 