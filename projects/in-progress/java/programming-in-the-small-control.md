# Chapter 3\. Programming in the Small II: Control

<http://math.hws.edu/javanotes/c3/index.html>

- What are blocks useful for?

  - Keeping temporary variables contained within the set of code that will use it, so that other statements cannot access that temporary variable and mess things up.

    ```java
    { // Switching the value of x and y
      int temp;   // A temporary variable for use in this block.
      temp = x;   // Save a copy of the value of x in temp.
      x = y;      // Copy the value of y into x. 
      y = temp;   // Copy the value of temp into y
    } // Outside of this block, statements cannot access temp as it will have been discarded/removed from memory
    ```

- Which loop do the `break` statements exit? What about `continue`?

  - The loop directly containing the `break` statements or `continue`, which exits the current iteration and starts at the beginning of the next iteration.

- How do you `break` out / `continue` past the direct loop?

  - Use a labeled `break` to exit the loop of interest or `continue` to exit out of the iteration of the desired loop.

- How do you create an infinite `for` loop?

  - `for ( initialization; continuation-condition; update)` - leave out the `continuation-condition` --> `for (;;)`

- How do I use a `try..catch` statement?

- How do I convert a string to an integer?

  - `Integer.valueOf(string)`

- What does it mean to **prime** a loop?

  - To make the condition that is supposed to start the loop true... before getting to the statements for the loop.

- How do I draw things?

- How do I check which element in the array has the largest number of divisors?

- How do I store values in an array?

- How do I ignore characters up to a certain point?

- How to convert a string into a number?

- How do I tell when a file has ended?

- How do I use the try..catch statement?

- What is a divisor?

  - A **divisor** of a number, N, is a number, D, that can divide N evenly so that there is no remainder. For instance, 2 is a divisor of 4 because `4/2` is 2 and the remainder is 0\. In other words, a divisor fits the following criteria: `N % D == 0`

- How do I determine the divisors of an integer?

**Section 3.5**

```java
package ch3Examples;

import textio.*;

/** Section 3.5 
 * This program will take inputs of units inches, feet, yards, or miles
 * and display the measurements in inches, feet, yards, and miles. 
 * http://math.hws.edu/javanotes/c3/s5.html
 *
 */
public class MeasurementConverter {

  public static void main(String[] args) {

    /* Declare the variables of interest */ 
    String input;   // The measurement that the user inputs
    double number;  // The quantitative portion of the measurement
                    // which will be converted in other units 
    String unit;    // The type of units
    double inches;    
    double feet; 
    double yards; 
    double miles; 

    /* Ask for user input */ 
    System.out.print("Input a measurement in in, ft, yds, miles: ");
    input = TextIO.getln(); 

    /* Separate the user input into the number entered and the unit type */ 
    // Skip the white spaces in input and read up until there is another white space; assign the value to variable number
    // Skip the white spaces and read the remaining letters into variable unit 
    // Convert variable unit into lower case letters. 

    /* Convert user input into inches, feet, yards, and miles */ 
    // IF the unit type is in inches, in the form in, inch, inches. 
      // Calculate ft as number divided by 12 
      // Calculate yards as number divided by 36
      // Calculate miles as number divided by 63360

    // ELSE IF the unit type is in feet, in the form ft, foot, feet: 
      // Calculate in as number times 12
      // Calculate yds as number divided by 3
      // Calculate miles as number divided 5280

    // ELSE IF the unit type is in yards, in the form 
      // Calculate in as number multiplied by 36
      // Calculate feet as number multiplied by 3
      // Calculate miles as number divided 1780

    // ELSE:
      // Calculate inches as number mulitplied by 63360
      // Calculate ft as number multiplied by 5280
      // Calculate yd as number multiplied by 1780

    /* Display the 4 results */ 


  } // end of main() 

} // end of class MeasurementConverter
```

## Section 3.6

- Why might you use a `switch` statement over an `if` statement?

  - The `switch` statement can be more efficient because the computer can skip statements until it gets to the branch where the case constant matches the value in the expression. In contrast, the `if` statement must evaluate the branches leading up to the desired branch before it executes, so there are more steps to process.
  - Creating menus.

## Section 3.7 Exceptions / Try..Catch

- What are **exceptions**?

  - Occurrences out of the norm that can crash the program. They are sometimes errors, but sometimes are not and can be considered a feature of the program, hence being called an exception rather than an error.

- What is a `NumberFormatException`?

  - A number format exception occurs when a string value can't be converted into an integer, because it's not a literal of a number, i.e. it can't represent a number. For instance, while `"11"` can represent the number 11, `Fred` cannot represent a number.

- What is a `IllegalArgumentException`?

  - An illegal argument exception occurs when the value passed into a subroutine isn't an acceptable parameter, e.g. If a subroutine requires arguments to be integers, then strings will be illegal.

- What does it mean for an exception to be _thrown_?

  - When an exception is thrown, an exception has occurred.
  - For instance, `Integer.parseInt(str)` _throws_ an exception of type `NumberFormatException` when the value of the str is not a number.

- What does it mean to _catch_ an exception?

  - To _catch_ an exception is to handle it in a way that prevents the program from crashing.

- What is the syntax for `try..catch` statements? Ideally, what happens if there is an exception?

  ```java
  try {
    // statements 
  } catch ( /* name-of-exception-class variable-name) */ ) {
    // statements 
  }
  ```

  - Ideally, the exception being thrown will be of the type defined in the catch statement. If so, then the program will skip from the line of code where the exception was thrown to the catch statement. Otherwise, if there are no catch blocks defined for the exception, then the program will crash.

- When might an exception be a good thing?

  - An exception might be a good thing if it is handled properly and can be used for another purpose. For instance, TextIO has a method to read lines from a file. When there are no more lines to read, an exception occurs. You can catch the exception and use it as a way to tell when the end of a file has been reached and either get input elsewhere or continue onward.

### Section 3.8 Intro to Arrays

- What is an **array**?

  - A data structure that chunks data items in a numbered sequence, such that each item can be referred to by its index, which is its position in the array starting from 0.

- What is **length**?

  - The number of items in an array.

- Why are arrays considered lists of _variables_ instead of lists of _values_?

  - The values in each position of an array can be changed, hence they are _variable_. In other words, each position in an array can store a value, so it is a variable.

- What is the syntax for creating arrays?

  ```java
  // Declare the variables 
  baseType[] arrayVariable; 
  // e.g.
  String[] nameList; 

  // Create the variable
  arrayVariable = new baseType[arrayLength]; 
  nameList = new String[1000]; // Create an array of type String with 1000 elements.
  ```

- What is an _integer-valued expression_?

  - An expression that evaluates to an integer.

- Why are arrays useful?

  - You can iterate through an array using a for loop because elements can be referenced by an integer variable or integer-valued expression. This process of iterating through the array can be used for many purposes, such as printing out a list, summing and averaging an array of numbers, finding the largest number, and other calculations.

    ```java
    /* This program will print out all the elements in an array */ 
    int i; // index of the array 
    for (i = 0; i < list.length; i++) {
      System.out.println( list[i] ); 
    }
    ```

- What is the difference between **sequential access** and **random access**?

  - Sequential access of arrays involves processing elements one by one, in order. By contrast, **random access** of arrays means that the difficulty of accessing an element is equal for any given element.

  - For instance, you could randomly generate a birthday between 0 and 364 and then check an array of boolean values to see if it's been generated before. Thus, any one of the elements in the boolean array would have an equal chance of being accessed. 
  
  - For an array, `used`, with 365 elements of type `boolean`, this loop will _randomly_ generate a number from 0-364, so each element has an equal chance of being accessed in each loop. 

    ```Java
    while (true) {
      int birthday; 
      birthday = (int)(Math.random()*365); 
      count++; 

      System.out.printf("Person %d has birthday number %d%n", count, birthday); 

      if ( used[birthday] ) {
        break; 
      }

      used[birthday] = true; 
    }
    ```

  - Can the size of arrays be changed? 

    - No. 

