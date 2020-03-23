# Coding in the Small: Syntax

- What should you do when reading the Java book?

  ```
  IF a new language feature is introduced, THEN:
        Memorize the **syntax**
        Practice using examples to build up understanding of **semantics**:
            How the features work
            Using the features in your own programs to test understanding
        Observe and practice **pragmatics**:
            Practice using good **style**
  ```

- What does a class need to be a program?

  - A `main` subroutine, e.g.

    ```
    public static void main(String[] args) {
          statements
      }
    ```

- **What are some style guidelines**

  - for names?

    - Names of **classes** begin with upper case letters, e.g. `HelloWorld`
    - Names of variables and subroutines begin with lower case letters, e.g. `lastName`, `skipBlanks()`
    - Avoid underscores in names and use camel case, e.g. `camelCase`

      - Declare one variable per line unless they're closely related.
      - Include a comment to explain the purpose of the variable
      - Declare important variables at the beginning of the subroutine with a comment to explain their purpose and unimportant variables where they are first used.

- What are **variables**?

  - Containers/boxes for data, but not the data themselves. The data in the box can change, so the same variable can hold different values at different times.

- What is an **expression**?

  - A data value or statement that boils down to a data value.

- What are the **primitive types**?

  - There are eight primitive types: byte, short, int, long, float, double, char, and boolean. They are grouped into two main categories and char and boolean by themselves
  - The primitives that hold integers are byte, short, int, and long ... ordered from least to greater capacity for representing numbers.

    - The **byte** data type holds one byte of memory, or 8 bits, or a set of 8 (0s or 1s), e.g. 10001000\. It can represent integers between and including -128 and 127\. 2**8 possible numbers = 256
    - **Short** holds 2 bytes (16 bits), so 2**16 ... between -32768 to 32767
    - **int** holds 4 bytes (32 bits), so 2**32... about negative two billion to positive two billion

  - The primitives that hold real numbers are float, double. Double holds more digits than float.

  - The primitive char holds a single character from the Unicode character set.

  - The boolean holds a true or false value.

- What are all data values represented as in a computer's memory?

  - A binary number, which is made up of bits and bytes:

    - A **bit** is a single 0 or 1.
    - A **byte** is a string of eight bits.

- Can primitive types represent all real numbers?

  - No, they can only represent numbers within a specified range, so pi would be unable to be represented or even 1/3 100% accurately.

- What are literals?

  - Constant values / representations of values, e.g. '' represents a string with no characters, e.g. To represent "Hello World!", you'd have to type the **literal**

    ```
    "\"Hello World!\""
    ```

- What are **enums**?

  - **Enums** are short for **enumerated types**, i.e. new classes of data that are limited to the defined set of values.
  - The syntax for enums is:

    ```java
    enum enumTypeName { list, of, enum, values }
    ```

    ```java
    enum Season { SPRING, SUMMER, FALL, WINTER }
    ```

  - Can enums be inside a subroutine?

    - No, enums need to be defined **outside** of the main() routine or inside a separate file.

  - Why are the possible values of an enum type called **enum constants**?

    - Enum values cannot be changed, post-definition.

- Which method is used to format output?

  - Using `printf`, specifically, `System.out.printf()`

  - What is the syntax for `printf`?

    - The are two parameters: How you want the output to be formatted and what you want to be formatted. The how goes first, and the syntax is `"%letter.optionalDecimalPlaces"`, where the quotes and `%` are constant to all `printf` statements and the `letter` can be `d`, `f`, `e`, etc depending on whether you want the output formatted as a double, float, or exponential respectively. The amount is the number input. The number after the `%letter.`, e.g. `%1.2f` would mean, "display the amount as a double with as many places as necessary and to the second decimal place."
    - For comma separation, e.g. to display `1,000,000,000.00`, you'd use the statement: `System.out.printf(",1.2f", 1000000000);`
    - To have output be left-justified, i.e. to have spaces come after the number, then use a negative at the beginning, e.g. to display '100 ': `System.out.printf("-7d", 100)`.

- What is a **static member**?

  - Static member variables and subroutines are those variables and subroutines that must include the name of their class when they are being called, e.g. the subroutine `exit` is a part of the class named `System`. Therefore, you'd write `System.exit` to refer to the `exit` subroutine.

- How do you re-route the standard output location for `TextIO`?

  - You can use the method `TextIO.writeFile("filename.txt");`. This method will create a file named "filename.txt" where your output will go.

- How do you have the user select the output file?

  - `TextIO.writeUserSelectedFile();` This will bring up a GUI for the user to select a file. When the user selects a file, the program returns a 1 and changes the standard output. Else, the program returns 0\.

- IF `N` is an integer variable and `N == 3`, then what is `N/2`? `2/N`? Why? How do you fix that _semantic_ error?

  - `1` and `0` respectively because the result of a calculation done on two integers will produce an integer. An integer cannot have numbers after the decimal, so the result is rounded down to the nearest integer.
  - To fix the error, you'd have one of the numbers be a real number, e.g. `2.0` for `2`. That way, when the calculation is done, N will be converted into a real number (i.e. `3.0`), so that the numbers after the decimal are kept.

- How do you use the **modulus** operator to check if a number is even or add?

  ```java
  int N = 3; 
  if ( N % 2 == 0) {
    System.out.print("The number, " + N + "is even."); 
  } else {
    System.out.print("The number, " + N + "is odd."); 
  }
  ```

- How is `y = x++;` different from `y = ++x`?

  - `y = x++;` will set the value of y to x and then increment the value of x. At the end of the calculation, the value of x will be greater than y by 1\.
  - `y = ++x;` will **increment** the value of x by 1 and then set assign the value of x to y. Thus, `y == x`, at the end.

- What is a conditional operator?

  - It is an expression of the form, 

    ```Java
    boolean-expression ? expression1 : expression2 
    /* IF the boolean-expression is TRUE, THEN 
      evaluate expression1, 
     ELSE 
      evaluate expression2
      */
    ```

- What does it mean to **type cast** a variable? How do you **type cast** a variable? 
  - To **type cast** a variable is to change the type of that variable, e.g. from `int` to `short`. It is used when you're trying to change the type of a variable to one which might not be able to hold the value, e.g. type casting 1000000 apparently gets you -31072. 
  - To **type cast** a variable, use the following syntax: 
  ```Java
  int anInteger; 
  short aShortie; 

  anInteger = 231; 
  aShortie = (short)(anInteger); // converts the type of anInteger into short and assigns the value to aShortie
  ```

