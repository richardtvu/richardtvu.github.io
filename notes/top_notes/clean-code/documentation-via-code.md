# [Code as documentation](https://www.martinfowler.com/bliki/CodeAsDocumentation.html)

- Why should the primary source of documentation be the code? 
  
    - By writing clear, readable code, there is 
        - *less overhead* in terms of looking up other, potentially outdated or missing, sources of documentation to understand the code ... 
        - a **guarantee** that the code is **up-to-date**, as the program *is* code.
            - By contrast, comments, diagrams, etc are not necessary for the code to run and therefore can be out-of-date.

- Why does the argument that most code bases are poor forms of documentation fail to invalidate the usefulness of code as documentation? 
    - Most code bases are poor forms of documentation because people did not put in the effort to make the code clean and understandable in the first place. Therefore, the documentation is poor because the documentation effort is poor. 
    - Documentation effort is a necessary condition for code bases to be useful forms of documentation. 

- How do you become better at writing readable and understandable code? 
    - Get feedback from others/code review. 
        - Pair program. 
    - Refactor code.
    - Adhere to the team style guidelines to ensure consistency and readability for teammates. 