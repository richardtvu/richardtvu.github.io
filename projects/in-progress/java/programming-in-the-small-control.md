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

- Which loop do the `break` statements exit?  What about `continue`?
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
    - A **divisor** of a number, N, is a number, D, that can divide N evenly so that there is no remainder. For instance, 2 is a divisor of 4 because `4/2` is 2 and the remainder is 0. In other words, a divisor fits the following criteria: 
        `N % D == 0`
        
- How do I determine the divisors of an integer?


**Section 3.5**

```Java
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
