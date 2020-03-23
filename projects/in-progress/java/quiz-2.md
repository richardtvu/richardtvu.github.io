# Quiz on Chapter 2

## Post Review

1. What I was missing is that a program with a syntax error will NOT run. However, a program with a semantic error WILL run, just not in the way you wanted it to. For instance since integers cannot contain decimals, the following will produce incorrect result `int frac = 1/3`, which will evaluate as `0`.

2. When a computer executes a variable declaration statement, it allocates some memory that can hold a specific amount of and type of data and associates it with a name. In other words, the computer makes a box to store stuff in and calls it a name that can be referenced later on. 

3. In programming, **type** refers to the possible values that can be contained within a variable. When you make a variable of a certain type, you're making a box that can store the values as defined byt he type. 

4. The boolean **type** is the set of two possible values, true and false. Booleans are used where true/false values are necessary, such as loops, if-statements, switch statements, comparisons, etc. 

5. OK!

6. Assignment statements are used to *change* the value of a variable. 

7. Precedence is a rule that the computer uses to decide on what operators get evaluated first. 

8. A **literal** is the set of characters representing a value. For instance the literal `"Hello, world!"` represents the String `Hello, World!` The actual value wouldn't include the quotes, but the quotes are needed for the computer to know that `Hello,` and `World` are part of the same string and that that string is a string!

9. `TextIO.getlnDouble()` is difference from `TextIO.getDouble()` in that it will discard the characters after the number, so it would discard a second number, or the white spaces, etc. 

10. OK!

11. OK! 

12. `String` is the name of a **class**, so it is colored differently in Eclipse than primitive types, such as int, double, and boolean. 

13. OK! 

14. 
# Attempt #1

1. Briefly explain what is meant by the syntax and the semantics of a programming language. Give an example to illustrate the difference between a syntax error and a semantics error.

  - **Syntax** is the structure of a programming language, kind of like grammar in a natural language like English. It dictates how tokens, like variables and operators are put together, just as grammar dictates how words in English are put together. By contrast, **semantics** govern the meaning of the program, what the program does or is intended to do, just as in English, someone trying to warn someone of danger might yell out "Fire! Run away!"

    - An example of a syntax error would be a misspelled word or an out of order sentence, e.g. "canidd" instead of "candid" or "man the is big" instead of "the man is big". In terms of programming, e.g. it would be like trying to call an undeclared variable or putting the condition for a while loop before the while:

      ```java
      int answerToLife = 42; 

      System.out.print("The answer to life is" + answer);  // answer hasn't been declared or initialized  

      ( answerToLife == 42) while {
      System.out.print("But what is the question to life?"); 
      break; 
      } // the condition is supposed to go after the while
      ```

2. What does the computer do when it executes a variable declaration statement. Give an example.

  - The computer creates a container for data of a certain type and allocates some memory to it and calls it by a name?

    - e.g. `string questionToLife = "What is the answer to life?"`

3. What is a type, as this term relates to programming?

  - **Type**, as it relates to programming, is the capacity of a variable to hold information and the constraint on which kinds of variables can be held.

    - e.g. `int` holds integers up to around +/- 2 billion
    - e.g. `char` holds a character

4. One of the primitive types in Java is boolean. What is the boolean type? Where are boolean values used? What are its possible values?

  - The boolean type is a container that holds data of the value true or false, i.e. 1 or 0 respectively. These boolean values are used in loops.

5. Give the meaning of each of the following Java operators:

  - a) `++` `// increment the variable adjacent and to the left of this operator by 1`

  - b) `&&` `The value to the left AND the value to the right`

  - c) `!=` `The value to the left is NOT EQUAL to the value to the right`

6. Explain what is meant by an assignment statement, and give an example. What are assignment statements used for?

  - An assignment statement is one in which a reference to a specific value is stored in a variable, e.g.

    ```java
    String greeting = "Good morning!"; // The reference to the string "Good morning" without the quotes is stored in a variable called greeting.
    ```

7. What is meant by precedence of operators?

  - Operators that take precedence over other operators will have their calculations performed prior to the other operators. i.e. Parentheses trump multiplication, so `(3 + 4) * 4` would equal `28`, even thought `*` has precedence over `+`.

8. What is a `literal`?

  - The plain text representation of a string, e.g. `\t` represents a tab; `\n` represents a new line; `"Hello World"` is the **literal** of `Hello World`.

9. In Java, classes have two fundamentally different purposes. What are they?

  - Classes can contain subroutines and variables that don't change, i.e. static variables.
  - Classes can also as a **type** to define **objects**. Classes define what objects generated from this type have in common, e.g. certain methods and static variables or variable names.

10. What is the difference between the statement `x = TextIO.getDouble();` and the statement `x = TextIO.getlnDouble();`

  - `getlnDouble()` will include a line feed at the end of the value input

11. Explain why the value of the expression 2 + 3 + "test" is the string "5test" while the value of the expression "test" + 2 + 3 is the string "test23". What is the value of "test" + 2 * 3 ?

  - Expressions evaluate from left to right, so `2+3` is added first and then converted into a string to add to `test`. If `test` is in the front, then everything after it gets converted. Since `*` has precedence over `+`, `"test" + 2 * 3` should evaluate as `test6`.

12. Integrated Development Environments such as Eclipse often use syntax coloring, which assigns various colors to the characters in a program to reflect the syntax of the language. A student notices that Eclipse colors the word String differently from int, double, and boolean. The student asks why String should be a different color, since all these words are names of types. What's the answer to the student's question?

  - **Strings** are objects, hence they are different from types that store numeric values. Need to look back at this!

13. What is the purpose of an import directive, such as `import textio.TextIO` or import `java.util.Scanner`?

  - Importing these classes allow you to use the subroutines or methods within those packages without writing them fully out each time, e.g. `import textio.TextIO` allows you use to call `TextIO.subroutineOfInterest` instead of `textio.TextIO.subroutineOfInterest` each time you want to use that subroutine.

  - WHat will `import java.util.Scanner` do?

14. Write a complete program that asks the user to enter the number of "widgets" they want to buy and the cost per widget. The program should then output the total cost for all the widgets. Use System.out.printf to print the cost, with two digits after the decimal point. You do not need to include any comments in the program.

```java
import textio.TextIO;

public class Widgets {

    public static void main(String[] args) {

        // ask user for # number of widgets 
        System.out.print("How many widgets? ");
        double numWidgets = TextIO.getlnDouble();
        System.out.print("Number of widgets input: "); 
        System.out.println(numWidgets); 
        // ask user for cost per widget 
        System.out.print("Cost per widget?" );
        double costPerWidget = TextIO.getlnDouble();
        System.out.print("Cost per widget input: ");
        System.out.println(costPerWidget); 
        // calculate total cost for all widges
        double totalCost; // cost of the widgets
        totalCost = numWidgets * costPerWidget; 
        // print the cost, with two digits after the decimal point
        System.out.print("The total cost of the widgets is $");
        System.out.printf( "%1.2f", totalCost);
    }
}
```

# Quiz 2 Try #2.

1. **Syntax** is the grammar of a programming language, basically how the programming words/tokens go together for them to make a coherent sentence. **Semantics** are the meaning of the code, what they're meant to do or communicate, like yelling "FIRE! RUN AWAY" is meant to communicate that people should avoid the scene and get out of the building because there's something dangerous.

  - An example of a syntax error would be like forgetting to enclose a string in quotation marks when trying to display it:

  ```java
  System.out.print("Hello, how are you?);
  /* You know that this command is meant to display the message "Hello, How are you?", but not having the end quotes will cause the program to be unable to be run */
  ```

  - An example of a semantics error would be like forgetting to enclose a block of code in parentheses when you're trying to make sure that they're run together in a loop:

  ```java
  boolean bool = true; 
  while (bool) 
   System.out.println("This the end.");
   if (bool) 
     bool = false;
  /* Without parentheses enclosing the while loop and including the if statement, bool will always be true, so there will be an infinite loop! */
  ```

## 2\. When the computer executes a variable declaration statement, it creates a variable of the specified type and allocates some memory for that variable. I think...

1. A **type**, as it relates to programming, is the constraint on what kind of data a variable can hold. For instance, a variable of type `int` can only hold integers from about negative two billion to about positive two billion and it cannot hold numbers with decimals. An `int` can hold the value `100`, but not the value `100.0`.

2. A **boolean** type is a variable that can hold the value of `0` or `1`, which is basically `true` or `false`. Boolean values are used in control structures, such as loops, and are used to determine whether a loop gets run.

3. The meaning of the `++` operator is to increment the value adjacent to it by one. The meaning of `&&` is AND, which will evaluate to the boolean value `true`, if and only if, both of the operands on either side of `&&` are true. Otherwise, an expression with `&&` will evaluate to false. The operator `!=` means "NOT EQUAL TO" and tests whether the two operands are not equal.

4. An **assignment statement** is a command to take a value, store it into some previously allocated memory, and then store the reference/address of that value in a variable. For instance, I can store the value of the current year in a variable called year by doing the following: `year = 2020;`. Assignment statements are used to store values in variables for later use.

5. **Precedence** of operators means the priority in which operators get evaluated: Higher precedence means faster evaluation.

## 8\. A literal is the form a value has to be typed as to be stored into a variable.

## 9\. Classes have two fundamentally different purposes. One of them is to create objects? Another is to provide a set of static variables and methods to objects?

1. The difference between `x = TextIO.getDouble();` and `x = TextIO.getlnDouble();` is that the first will get the input of the user, skipping white spaces until it hits the first white space or carriage return, and then it will store the rest of the user input in the input buffer to be used later. The second statement will get the user's input until it hits the first white space/carriage return and discard the rest of the input. The first is used if you want to the user to be able to input multiple answers on the same line/file. By contrast, the second is used when you only want to have one input per line.

2. `2 + 3 + "test"` will be `"5test"` because expressions are evaluated from left to right when precedence is equal. Thus, the `2+3` will evaluate as `5` and then the `5` will get converted into a string so that it can be added to `"test"`. By contrast, `"test" + 2 + 3` will be `"test23"` because `2` will get converted to a string, then added to `"test"` to become `"test2"` and the same will happen with `3` to become `"test23"`. Following this logic, `"test" + 2*3` should be `"test6"` because multiplication has a higher precedence than addition.

## 12\. The type **String** is colored differently from the types **int, double,** and **boolean** because strings are objects which have their own methods, whereas the other variables are primitive types without their own methods.

1. The purpose of the import directive, such as `import textio.TextIO` or `import java.util.Scanner` is to make the classes and their respective methods available in the current class, e.g. to use `TextIO.getlnInt()`.

2. I made a widget pricer with and without the scanner method

```java
import textio.TextIO;

public class PriceWidgets {

    public static void main(String[] args) {

        int widgets; 
        double cost; 
        double totalCost; 

        System.out.print("How many widgets do you want?    "); 
        widgets = TextIO.getlnInt();

        System.out.print("How much does each widget cost?  "); 
        cost = TextIO.getlnDouble();

        totalCost = widgets * cost; 

        System.out.printf("The total cost of all of the widgets is "
                + "$%1.2f%n", totalCost); 
    }

}
```

```java
package quizPrograms;

/** Quiz 2 Question #14
 * This program will ask the user for the number of widgets that they want to
 * buy and the cost per widget. Then, it will output the total cost for 
 * all of the widgets using System.out.printf. The output will have two digits
 * after the decimal point. 
 */

import java.util.Scanner;

public class PriceWidgetsWithScanner {

    public static void main(String[] args) {

        /* Create a scanner object, which will be used to get user input */ 
        Scanner stdin = new Scanner( System.in );  

        int widgets;         // Number of widgets to purchase, input by user
        double cost;         // The cost of each widget, in dollars 
        double totalCost;     // Total cost for all of the widgets

        System.out.print("How many widgets do you want to purchase?    ");
        widgets = stdin.nextInt();     
        stdin.nextLine(); 

        System.out.print("How much, in dollars, do each widget cost?   "); 
        cost = stdin.nextDouble();
        stdin.nextLine(); 

        totalCost = widgets * cost; 

        System.out.printf("The total cost for all of the widgets is"
                + " $%1.2f%n", totalCost); 

    }
}
```
